import unittest

import src.watch.router as router


class BasicTest(unittest.TestCase):
    """Test basic functionality for "watch" route."""

    def test_base(self):
        """Test basic."""
        self.assertEqual(router.watch_http(), "Watch")
