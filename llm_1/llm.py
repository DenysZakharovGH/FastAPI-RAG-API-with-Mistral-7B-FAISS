from sympy.physics.units import temperature
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_name = "mistralai/Mistral-7B-Instruct-v0.2"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    device_map="auto")

# prompt = """You are a senior Python engineer.
# """
#
# inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
# outputs = model.generate(**inputs, max_new_tokens=50)
#
# print(tokenizer.decode(outputs[0], skip_special_tokens=True))
def generate_answer1(prompt: str, max_new_tokens: int = 100):

    answer = "I am the LLM answer"

    return answer

def generate_answer(prompt: str, max_new_tokens: int = 100) -> str:
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(**inputs,
                             max_new_tokens=max_new_tokens,

                             )

    # generated_tokens = outputs[0][inputs["input_ids"].shape[-1]:]

    return tokenizer.decode(outputs[0], skip_special_tokens=True)
