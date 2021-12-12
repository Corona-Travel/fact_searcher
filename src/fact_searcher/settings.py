from functools import lru_cache
from typing import Any

from pydantic import AnyUrl, BaseSettings


class Settings(BaseSettings):
    facts_url: Any = "http://localhost:1234/"

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()
