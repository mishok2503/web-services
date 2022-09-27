import unittest

import src.delete.router as router


class BasicTest(unittest.TestCase):
    """Test basic functionality for "delete" route."""

    def test_base(self):
        """Test basic."""
        self.assertEqual(router.delete_http(), "Delete")
