from fastapi import Depends, APIRouter, Request, Body

from app.core.config import settings
from app.llm_1.rag import answer_with_rag_async
from app.pydentic_models.models import AskResponse, AskRequest
from slowapi import Limiter
from slowapi.util import get_remote_address
llm_route = APIRouter()
limiter = Limiter(key_func=get_remote_address)


@llm_route.post("/ask", response_model=AskResponse)
@limiter.limit(settings.llm.rate_limits)
async def ask(
        request: Request,
        req: AskRequest = Body()) -> AskResponse:
    answer, sources = await answer_with_rag_async(req.question)
    return AskResponse(
        answer=answer,
        sources=sources
    )