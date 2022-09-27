from fastapi import APIRouter, Response, status
from fastapi.responses import JSONResponse

from src.database.database import database

router = APIRouter()


@router.get("", response_class=JSONResponse)
def info_http(video_id: int, response: Response) -> str:
    """Meta info about video.

    Args:
        video_id (int): video id

    Returns:
        json: video info or error TODO: jsonschema
    """
    video = database.get_video(video_id)
    if not video:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"status": "video not found"}
    return {"status": "success", "info": video.to_json()}
