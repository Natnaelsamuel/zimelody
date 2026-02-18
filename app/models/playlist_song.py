import uuid
from datetime import datetime, timezone

from sqlalchemy import DateTime, ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, generate_uuid


class PlaylistSong(Base):
    """
    Join table between Playlist and Song.
    Enables songs to have a specific order within a playlist.
    """
    __tablename__ = "playlist_songs"
    __table_args__ = (
        UniqueConstraint("playlist_id", "song_id", name="uq_playlist_song"),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=generate_uuid,
    )
    playlist_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("playlists.id", ondelete="CASCADE"),
        nullable=False,
    )
    song_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("songs.id", ondelete="CASCADE"),
        nullable=False,
    )
    position: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
    )
    added_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    # ── Relationships ─────────────────────────────────────────
    playlist: Mapped["Playlist"] = relationship(
        "Playlist",
        back_populates="songs",
    )
    song: Mapped["Song"] = relationship(
        "Song",
        back_populates="playlist_entries",
    )