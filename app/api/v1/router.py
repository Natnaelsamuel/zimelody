from fastapi import APIRouter

# This is the "Main Hub" for all v1 routes.
# We'll connect auth_router, song_router, etc. here later.
router = APIRouter(prefix="/api/v1")