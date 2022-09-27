from fastapi import APIRouter

router = APIRouter()


@router.get("")
def delete_http() -> str:
    """Delete video."""
    return "Delete"
