from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="", env_file=None)
    database_url: str = Field(
        default="postgresql+psycopg://traderai:traderai_local_password@localhost:5432/traderai",
        alias="DATABASE_URL",
    )
    redis_url: str = Field(default="redis://localhost:6379/0", alias="REDIS_URL")
    ready_timeout_seconds: float = 1.0


def get_settings() -> Settings:
    return Settings()
