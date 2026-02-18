import enum
import uuid

from sqlalchemy import Boolean, Enum, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin, generate_uuid


class UserRole(str, enum.Enum):
    """
    User roles as a Python + PostgreSQL enum.
    Inheriting from 'str' lets us use the roles as strings in our API easily.
    """
    LISTENER = "listener"
    ARTIST = "artist"
    ADMIN = "admin"


class User(Base, TimestampMixin):
    """Core identity table. Every person in ZiMelody is a User."""
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=generate_uuid,
    )
    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
        nullable=False,
    )
    username: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        index=True,
        nullable=False,
    )
    hashed_password: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    role: Mapped[UserRole] = mapped_column(
        Enum(UserRole, name="user_role", create_constraint=True),
        default=UserRole.LISTENER,
        nullable=False,
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    # ── Relationships ─────────────────────────────────────────
    # These link to models we'll create next. 
    # SQLAlchemy lets us use string names like "ArtistProfile" 
    # so we don't have circular import issues.
    artist_profile: Mapped["ArtistProfile"] = relationship(
        "ArtistProfile",
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan",
    )
    playlists: Mapped[list["Playlist"]] = relationship(
        "Playlist",
        back_populates="user",
        cascade="all, delete-orphan",
    )
    likes: Mapped[list["Like"]] = relationship(
        "Like",
        back_populates="user",
        cascade="all, delete-orphan",
    )
    play_history: Mapped[list["PlayHistory"]] = relationship(
        "PlayHistory",
        back_populates="user",
        cascade="all, delete-orphan",
    )