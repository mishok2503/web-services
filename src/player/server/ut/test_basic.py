import unittest

from src.player.server.server import PlayerBackendServicer
from player_pb2 import PlayerVersion, Null


class TestBasic(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(
            PlayerVersion(version=1, sub_version=0),
            PlayerBackendServicer().get_player_version(Null()),
        )
