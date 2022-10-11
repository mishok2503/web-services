set -x

export PROTOS_PATH=${PROTOS_PATH="src/common/protos/"}
export PLAYER_PATH=${PLAYER_PATH="src/player/server/"}

python -m grpc_tools.protoc -I $PROTOS_PATH --python_out=$PLAYER_PATH --grpc_python_out=$PLAYER_PATH player.proto
python -m grpc_tools.protoc -I $PROTOS_PATH --python_out=. --grpc_python_out=. player.proto
