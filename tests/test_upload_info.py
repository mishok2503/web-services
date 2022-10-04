import unittest
from typing import Tuple

from fastapi import Response

import src.info.router as info_router
import src.upload.router as upload_router
from src.common.types.video import Video
from src.database.database import database


class TestUploadInfo(unittest.TestCase):
    def _get_info(self, v_id: int) -> Tuple[int, str]:
        res = Response()
        body = info_router.info_http(v_id, res)
        return res.status_code, body

    def _test_200(self, v_id: int, name: str, desc: str = ""):
        c, b = self._get_info(v_id)
        self.assertEqual(c, 200)
        self.assertEqual(
            b, {"status": "success", "info": Video(v_id, name, desc).to_json()}
        )

    def _test_404(self, v_id: int):
        c, b = self._get_info(v_id)
        self.assertEqual(c, 404)
        self.assertEqual(b, {"status": "video not found"})

    def test_200(self):
        database.clear()
        self._test_404(1)
        self.assertEqual(upload_router.upload_http("testname", "test")["id"], 1)
        self._test_200(1, "testname", "test")
        self.assertEqual(upload_router.upload_http("name", "test")["id"], 2)
        self._test_404(3)
        self.assertEqual(upload_router.upload_http("test_name")["id"], 3)
        self._test_200(3, "test_name")
        self.assertEqual(upload_router.upload_http("test name", "_")["id"], 4)
        self._test_200(4, "test name", "_")
        self._test_404(239)
