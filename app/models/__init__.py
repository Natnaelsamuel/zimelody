# Registration point for all models
from app.models.base import Base  # noqa: F401
from app.models.user import User, UserRole  # noqa: F401
from app.models.artist_profile import ArtistProfile  # noqa: F401
from app.models.song import Song  # noqa: F401
from app.models.playlist import Playlist  # noqa: F401
from app.models.playlist_song import PlaylistSong  # noqa: F401
from app.models.like import Like  # noqa: F401
from app.models.play_history import PlayHistory  # noqa: F401