import faiss
import pickle

import numpy as np
from sentence_transformers import SentenceTransformer
from typing import List

from starlette.concurrency import run_in_threadpool

from app.core.config import DATA_STORAGE
from app.llm_1.llm import generate_answer

index = faiss.read_index(F"{DATA_STORAGE}/faiss_index.bin")
model = SentenceTransformer("all-MiniLM-L6-v2")
# Metadata

with open(F"{DATA_STORAGE}/faiss_metadata.pkl", "rb") as f:
    metadata = pickle.load(f)



def get_context_data(query_text: str) -> (List[str], List[str]):
    query_emb = model.encode([query_text])
    query_emb /= np.linalg.norm(query_emb, axis=1, keepdims=True)  # normalise a vector

    D, I = index.search(query_emb, k=3)

    print("D, I", D, I)

    # for idx, score in zip(I[0], D[0]):
    #     print(f"Text: {metadata[idx]}, Score: {score}")

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
            
            ### CONTEXT:
            {context}
            
            ### QUESTION:
            {question}
            [/INST]
            """

def answer_with_rag(question: str,) -> (str, List[str]):
    context, source = get_context_data(question)
    prompt = build_rag_prompt(context, question)
    answer = generate_answer(prompt)

    return answer, source

async def answer_with_rag_async(question: str) -> (str, List[str]):
    context, source  = get_context_data(question)
    prompt = build_rag_prompt(context, question)

    answer = await run_in_threadpool(generate_answer, prompt)

    return answer, source