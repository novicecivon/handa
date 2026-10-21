from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings, read from environment variables prefixed with HANDA_."""

    model_config = SettingsConfigDict(env_prefix="HANDA_", env_file=".env", extra="ignore")

    env: str = "local"
    database_url: str = "postgresql+psycopg://handa:handa@localhost:5432/handa"
    pilot_area: str = "marikina"


@lru_cache
def get_settings() -> Settings:
    return Settings()
