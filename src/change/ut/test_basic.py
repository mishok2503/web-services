import unittest

import src.change.router as router


class BasicTest(unittest.TestCase):
    """Test basic functionality for "change" route."""

    def test_base(self):
        """Test basic."""
        self.assertEqual(router.change_http(), "Change")
