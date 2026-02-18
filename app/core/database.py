from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.core.config import get_settings

settings = get_settings()

# Engine — the actual connection to PostgreSQL
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    echo=settings.DEBUG,
)

# Session Factory — creates new database sessions
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)


# FastAPI Dependency — gives each request its own session
def get_db() -> Generator[Session, None, None]:
    """Yields a database session, then closes it after the request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()