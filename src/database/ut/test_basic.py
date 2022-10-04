import unittest

from src.common.types.video import Video
from src.database.database import DataBase


class TestBasic(unittest.TestCase):
    """Test database basic functionality."""

    def setUp(self):
        self.cur_v_id = 0
        self.db = DataBase()

    def _insert_get(self, name: str, desc: str = ""):
        self.cur_v_id += 1
        self.assertEqual(self.db.insert_video(name, desc), self.cur_v_id)
        self.assertEqual(
            self.db.get_video(self.cur_v_id), Video(self.cur_v_id, name, desc)
        )

    def test_insert_get(self):
        self._insert_get("test_name")
        self._insert_get("some_name", "smthg")
        self._insert_get("new_name", "This is video")
