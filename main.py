import time
import uuid
import uvicorn
from fastapi import FastAPI, Request

from llm_1.rag import answer_with_rag, answer_with_rag_async
from pydentic_models.models import AskResponse, AskRequest
from core.config import settings
from core.logs import logger

app = FastAPI()


@app.get("/")
def confirm_server_alive():
    return {"msg": "Stay alive"}


@app.post("/ask", response_model=AskResponse)
async def ask(req: AskRequest):
    answer, sources = await answer_with_rag_async(req.question)
    return AskResponse(
        answer=answer,
        sources=sources
    )


@app.middleware("http")
async def request_logging_middleware(request: Request, call_next):
    request_id = str(uuid.uuid4())
    request.state.request_id = request_id

    start = time.perf_counter()
    response = await call_next(request)
    duration = time.perf_counter() - start

    logger.info(
        "[%s] %s %s %.3fs",
        request_id,
        request.method,
        request.url.path,
        duration,
    )

    response.headers["X-Request-ID"] = request_id
    return response


if __name__ == "__main__":
    uvicorn.run("main:app",
                host=settings.run.host,
                port=settings.run.port)




