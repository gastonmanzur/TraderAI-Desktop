from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    market_data_mode: str = "fake"
