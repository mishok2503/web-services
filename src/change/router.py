from fastapi import APIRouter

router = APIRouter()


@router.get("")
def change_http() -> str:
    """Change video."""
    return "Change"
