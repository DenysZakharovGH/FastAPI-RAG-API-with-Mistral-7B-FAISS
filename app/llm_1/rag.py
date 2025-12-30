import json

import faiss
import pickle

import numpy as np
from llama_cpp import Llama
from sentence_transformers import SentenceTransformer
from typing import List

from app.core.config import DATA_STORAGE, settings

index = faiss.read_index(F"{DATA_STORAGE}/faiss_index.bin")
model = SentenceTransformer("all-MiniLM-L6-v2")
# Metadata

with open(F"{DATA_STORAGE}/faiss_metadata.pkl", "rb") as f:
    metadata = pickle.load(f)


llm_model = Llama(
    model_path=F"{DATA_STORAGE}/mistral-7b-instruct-v0.2.Q4_K_M.gguf",
    n_ctx=8192,
    n_threads=8,
    n_gpu_layers=35,
    n_batch=512,      # ⚡ faster token processing
    use_mlock=True,   # ⚡ avoid memory paging
    use_mmap=True,
)

def get_context_data(query_text: str) -> (List[str], List[str]):
    query_emb = model.encode([query_text])
    query_emb /= np.linalg.norm(query_emb, axis=1, keepdims=True)  # normalise a vector

    D, I = index.search(query_emb, k=3)

    context = "/n".join(metadata[idx]["text"] for idx, score in zip(I[0], D[0]))
    source = [metadata[idx]["text"] for idx, score in zip(I[0], D[0])]
    print("context", context)

    return context, source


def build_rag_prompt(context: str, question: str) -> str:
    return f"""
            <s>[INST]
            You are a highly knowledgeable assistant.
            
            - ONLY use the information provided in the context!
            - If the answer is not in the context, reply exactly with: "I don't know".
            - Answer in one short, clear, and meaningful sentence.
            - Do not add extra explanations, opinions, or information beyond the context.
            - Provide information what you have learned from context to make that answer.
            
            ### CONTEXT:
            {context}
            
            ### QUESTION:
            {question}
            [/INST]
            """


async def answer_with_rag_stream(question: str):
    context, source  = get_context_data(question)
    prompt = build_rag_prompt(context, question)

    stream = llm_model(
        prompt,
        max_tokens=settings.llm.max_token_limits,
        temperature=settings.llm.temperature,
        stream=True,
    )

    # 4. Yield tokens as they arrive
    for chunk in stream:
        delta = chunk["choices"][0]["text"]
        if delta:
            yield json.dumps({"token": delta}) + "\n"

