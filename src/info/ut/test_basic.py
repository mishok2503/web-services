import unittest
from typing import Tuple

from fastapi import Response
from parameterized import parameterized

import src.info.router as router


class BasicTest(unittest.TestCase):
    """Test basic functionality for "info" route."""

    def _get_info(self, v_id: int) -> Tuple[int, str]:
        res = Response()
        body = router.info_http(v_id, res)
        return res.status_code, body

    @parameterized.expand([[1], [239], [42]])
    def test_404(self, v_id: int):
        c, b = self._get_info(v_id)
        self.assertEqual(c, 404)
        self.assertEqual(b, {"status": "video not found"})
