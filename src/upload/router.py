from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.database.database import database

router = APIRouter()


@router.get("", response_class=JSONResponse)
def upload_http(name: str, description: str = "") -> int:
    """Upload video."""
    return {"id": database.insert_video(name, description)}
