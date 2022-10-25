import json
import unittest

from kafka3 import KafkaProducer

from src.telemetry_read.reading import main


class TestBrokerReader(unittest.TestCase):
    """Test reading from Kafka."""

    def test_parsing(self):
        producer = KafkaProducer(bootstrap_servers="localhost:9092")
        producer.bootstrap_connected()
        expected_db = {
            (239, 143): 42,
            (14, 15): 16,
            (555, 444): 1.234,
            (1234, 431): 123.123,
        }
        db = {}
        for key, value in expected_db.items():
            j = {"user_id": key[0], "video_id": key[1], "time": value}
            producer.send("player-telemetry", bytes(json.dumps(j), "utf-8"))

        main(db, len(expected_db))

        self.assertEqual(db, expected_db)
