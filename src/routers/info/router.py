from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("", response_class=JSONResponse)
def info_http(video_id: int) -> str:
    """Meta info about video."""
    return {"name": "ABC", "description": "BCA", "id": video_id}
