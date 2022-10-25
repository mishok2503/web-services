import json
from typing import Dict
from kafka3 import KafkaConsumer


def main(database: Dict, need_msgs: int = -1):
    """Read data from topic and write it to DB."""
    consumer = KafkaConsumer(
        "player-telemetry",
        bootstrap_servers="localhost:9092",
        auto_offset_reset="earliest",
        value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    )
    for msg in consumer:
        data = msg.value
        database[(data["user_id"], data["video_id"])] = data["time"]
        if need_msgs >= 0:
            need_msgs -= 1
            if need_msgs <= 0:
                break


db = {}

if __name__ == "__main__":
    main(db)
