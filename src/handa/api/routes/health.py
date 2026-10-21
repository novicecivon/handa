from fastapi import APIRouter
from pydantic import BaseModel

from handa import __version__
from handa.config import get_settings

router = APIRouter(tags=["health"])


class Health(BaseModel):
    status: str
    version: str
    pilot_area: str


@router.get("/health", response_model=Health)
def health() -> Health:
    settings = get_settings()
    return Health(status="ok", version=__version__, pilot_area=settings.pilot_area)
