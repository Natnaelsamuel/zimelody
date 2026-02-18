from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables / .env file.

    Using pydantic-settings gives us:
    - Automatic type coercion (e.g., str → int for port)
    - Validation at startup (fail fast if config is missing)
    - A single source of truth for all config values
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    # ── Database ──────────────────────────────────────────────
    DATABASE_URL: str

    # ── JWT ───────────────────────────────────────────────────
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # ── App ───────────────────────────────────────────────────
    APP_NAME: str = "ZiMelody"
    DEBUG: bool = False


@lru_cache()
def get_settings() -> Settings:
    """
    Cached settings instance — parsed once, reused everywhere.

    Why lru_cache?
    Reading .env and validating happens only on the first call.
    Every subsequent call returns the same object instantly.
    This is the recommended pattern from FastAPI docs.
    """
    return Settings()

