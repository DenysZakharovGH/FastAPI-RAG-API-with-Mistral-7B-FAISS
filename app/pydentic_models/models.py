from fastapi.temp_pydantic_v1_params import Query
from pydantic import BaseModel

from app.core.config import settings


class AskRequest(BaseModel):
    question: str = Query(...,
                          description="The question to ask",
                          min_length=1,
                          max_length=settings.llm.user_input_limits)


class AskResponse(BaseModel):
    answer: str
    sources: list[str]