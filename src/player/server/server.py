from concurrent.futures import ThreadPoolExecutor

import grpc
from player_pb2 import PlayerVersion
from player_pb2_grpc import PlayerBackendServicer, add_PlayerBackendServicer_to_server


class Service(PlayerBackendServicer):
    """GRPC player backend."""

    def get_player_version(self, request, context):
        """Return default player version."""
        return PlayerVersion(version=1, sub_version=0)


def execute_server():
    """Run gRPC server."""
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    add_PlayerBackendServicer_to_server(Service(), server)
    server.add_insecure_port("[::]:3000")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    execute_server()
