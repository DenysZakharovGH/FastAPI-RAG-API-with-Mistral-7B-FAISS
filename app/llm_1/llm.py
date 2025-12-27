from llama_cpp import Llama
from sympy.physics.units import temperature
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

from app.core.config import DATA_STORAGE

model = Llama(
    model_path=F"{DATA_STORAGE}/mistral-7b-instruct-v0.2.Q4_K_M.gguf",
    n_ctx=8192,
    n_threads=8,
    n_gpu_layers=35,  # якщо є GPU
)

def generate_answer1(prompt: str, max_new_tokens: int = 100):

    answer = "I am the LLM answer"

    return answer

def generate_answer(prompt: str, max_new_tokens: int = 100) -> str:

    output = model(prompt, max_tokens=max_new_tokens,)

    return output["choices"][0]["text"]



