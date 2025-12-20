
import uvicorn
from fastapi import FastAPI

from llm_1.rag import answer_with_rag, answer_with_rag_async
from pydentic_models.models import AskResponse, AskRequest

app = FastAPI()


@app.get("/")
def confirm_server_alive():
    return {"msg": "Stay alive"}

@app.post("/ask", response_model=AskResponse)
async def ask(req: AskRequest):
    #answer, sources = answer_with_rag(req.question)

    answer, sources = await answer_with_rag_async(req.question)

    return AskResponse(
        answer=answer,
        sources=sources
    )


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000)




