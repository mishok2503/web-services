from fastapi import APIRouter

router = APIRouter()


@router.get("")
def uploadi_http() -> str:
    """Upload video."""
    return 1
