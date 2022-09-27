from fastapi import APIRouter

router = APIRouter()


@router.get("")
def watch_http() -> str:
    """Watch video."""
    return "Watch"
