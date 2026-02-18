import uuid
from datetime import datetime, timezone

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, generate_uuid


class Song(Base):
    """
    A song uploaded by an artist.
    """
    __tablename__ = "songs"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=generate_uuid,
    )
    artist_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("artist_profiles.id", ondelete="CASCADE"),
        nullable=False,
    )
    title: Mapped[str] = mapped_column(
        String(255),
        index=True,
        nullable=False,
    )
    genre: Mapped[str | None] = mapped_column(
        String(100),
        index=True,
        nullable=True,
    )
    audio_file_url: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )
    cover_image_url: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )
    duration_seconds: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )
    play_count: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    # ── Relationships ─────────────────────────────────────────
    artist: Mapped["ArtistProfile"] = relationship(
        "ArtistProfile",
        back_populates="songs",
    )
    likes: Mapped[list["Like"]] = relationship(
        "Like",
        back_populates="song",
        cascade="all, delete-orphan",
    )
    playlist_entries: Mapped[list["PlaylistSong"]] = relationship(
        "PlaylistSong",
        back_populates="song",
        cascade="all, delete-orphan",
    )
    play_history: Mapped[list["PlayHistory"]] = relationship(
        "PlayHistory",
        back_populates="song",
        cascade="all, delete-orphan",
    )