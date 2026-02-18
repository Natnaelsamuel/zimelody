import uuid
from datetime import datetime, timezone

from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, generate_uuid


class ArtistProfile(Base):
    """
    Extended profile for users with the 'artist' role.
    This follows the Single Responsibility Principle:
    - User table handles identity
    - ArtistProfile handles artist-specific public data
    """
    __tablename__ = "artist_profiles"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=generate_uuid,
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        unique=True,  # This enforces the one-to-one relationship
        nullable=False,
    )
    stage_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )
    bio: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )
    profile_image_url: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    # ── Relationships ─────────────────────────────────────────
    user: Mapped["User"] = relationship(
        "User",
        back_populates="artist_profile",
    )
    songs: Mapped[list["Song"]] = relationship(
        "Song",
        back_populates="artist",
        cascade="all, delete-orphan",
    )