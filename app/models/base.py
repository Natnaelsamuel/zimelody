import uuid
from datetime import datetime, timezone

from sqlalchemy import DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """Base class for all ZiMelody models."""
    pass


class TimestampMixin:
    """
    Mixin that adds created_at and updated_at columns.
    Not every table needs both (e.g., PlayHistory is append-only),
    so we use a mixin instead of putting these on Base.
    """

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False,
    )


def generate_uuid() -> uuid.UUID:
    """Generate a new UUID v4 for use as a primary key."""
    return uuid.uuid4()