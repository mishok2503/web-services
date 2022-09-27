import unittest
import json

import src.upload.router as router


class BasicTest(unittest.TestCase):
    """Test basic functionality for "upload" route."""

    def test_base(self):
        """Test basic."""
        self.assertEqual(router.upload_http("some name")["id"], 1)
