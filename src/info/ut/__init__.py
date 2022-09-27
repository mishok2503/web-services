import unittest

import src.info.router as router


class BasicTest(unittest.TestCase):
    """Test basic functionality for "info" route."""

    def test_base(self):
        """Test basic."""
        self.assertEqual(router.info_http(), {"name": "ABC"})
