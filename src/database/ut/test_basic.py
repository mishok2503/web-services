import unittest

from parameterized import parameterized

from src.common.types.video import Video
from src.database.database import DataBase


class TestBasic(unittest.TestCase):
    """Test database basic functionality."""

    def setUp(self):
        self.cur_v_id = 0
        self.db = DataBase()

    @parameterized.expand(
        [["test_name"], ["some_name", "smthg"], ["new_name", "This is video"]]
    )
    def test_insert_get(self, name: str, desc: str = ""):
        self.cur_v_id += 1
        self.assertEqual(self.db.insert_video(name, desc), self.cur_v_id)
        self.assertEqual(
            self.db.get_video(self.cur_v_id), Video(self.cur_v_id, name, desc)
        )
