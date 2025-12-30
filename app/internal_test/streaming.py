from app.llm_1.llm import generate_answer, model
import time


question = "What is a RAG?"


stream = model(
    question,
    max_tokens=512,
    temperature=0.7,
    stream=True,
)

# Consume tokens as they arrive
for chunk in stream: # generator
    if "choices" in chunk:
        delta = chunk["choices"][0]["text"]
        if delta:
            print(delta, end="", flush=True)

exit()
start_time = time.time()
llm_answer = generate_answer(question)
print(llm_answer, time.time() - start_time)  # 31.424734115600586

#
# {
#   "id": "cmpl-xxxx",
#   "object": "text_completion",
#   "choices": [
#     {
#       "text": "Hello",
#       "index": 0,
#       "logprobs": None,
#       "finish_reason": None
#     }
#   ]
# }