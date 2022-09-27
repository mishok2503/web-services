from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("", response_class=JSONResponse)
def info_http() -> str:
    """Meta info about video."""
    return {"name": "ABC"}
