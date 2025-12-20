from typing import Set

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel
from pathlib import Path


BASE_DIR = Path(__file__).parent.parent.parent


class RunConfig(BaseModel):
    #host: str = "127.0.0.1"
    host: str = "192.168.2.40"
    port: int = 8000

class LLMConfig(BaseModel):
    rate_limits: int = 20
    max_token_limits: int = 400
    treshold_answer_similarity: float = 0.5

class Setting(BaseSettings):
    db_echo: bool = True  # settings variable to use for settings of our current DB
    run: RunConfig = RunConfig()
    llm: LLMConfig = LLMConfig()

settings = Setting()

