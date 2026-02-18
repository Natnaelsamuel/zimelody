import uuid

from sqlalchemy import Boolean, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin, generate_uuid


class Playlist(Base, TimestampMixin):
    """A user-curated collection of songs."""
    __tablename__ = "playlists"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=generate_uuid,
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    )
    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )
    is_public: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    # ── Relationships ─────────────────────────────────────────
    user: Mapped["User"] = relationship(
        "User",
        back_populates="playlists",
    )
    # Note: This points to the join table we're about to create
    songs: Mapped[list["PlaylistSong"]] = relationship(
        "PlaylistSong",
        back_populates="playlist",
        cascade="all, delete-orphan",
        order_by="PlaylistSong.position",
    )