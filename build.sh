set -x

export PROTOS_PATH=${PROTOS_PATH="src/common/protos/"}

pushd $PROTOS_PATH
python -m grpc_tools.protoc -I . player.proto --python_out=. --grpc_python_out=.
popd
