import grpc
from fastapi import APIRouter

from player_pb2_grpc import PlayerBackendStub
from player_pb2 import Null

router = APIRouter()


@router.get("")
def watch_http() -> str:
    """Watch video."""
    with grpc.insecure_channel("localhost:3000") as channel:
        client = PlayerBackendStub(channel)
        version = client.get_player_version(Null())

    return f"Player version: {version.version}.{version.sub_version}"
