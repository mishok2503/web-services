import unittest

from parameterized import parameterized

import src.upload.router as router


class BasicTest(unittest.TestCase):
    """Test basic functionality for "upload" route."""

    @parameterized.expand([["some name", 1], ["more name", 2], ["new name", 3]])
    def test_base(self, name: str, v_id: int):
        self.assertEqual(router.upload_http(name)["id"], v_id)
