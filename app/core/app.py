from fastapi import Depends, APIRouter, Request, Body
from fastapi.responses import StreamingResponse

from app.core.config import settings
from app.llm_1.rag import answer_with_rag_stream
from app.pydentic_models.models import AskResponse, AskRequest
from slowapi import Limiter
from slowapi.util import get_remote_address
llm_route = APIRouter()
limiter = Limiter(key_func=get_remote_address)


@llm_route.post("/ask")
@limiter.limit(settings.llm.rate_limits)
async def ask(
        request: Request,
        req: AskRequest = Body()):

    async def token_stream():
        async for chunk in answer_with_rag_stream(req.question):
            yield chunk

    return StreamingResponse(
        token_stream(),
        media_type="application/json",
    )