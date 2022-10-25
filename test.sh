trap 'kill $(jobs -p)' EXIT


docker compose -f src/telemetry_read/docker-compose.yaml up >/dev/null &
python src/player/server/server.py &


sleep 5

python -m unittest
docker compose -f src/telemetry_read/docker-compose.yaml down
