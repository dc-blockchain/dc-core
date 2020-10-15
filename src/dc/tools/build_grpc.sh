#!/usr/bin/env bash
pushd . > /dev/null
cd $( dirname "${BASH_SOURCE[0]}" )
cd ..

python -m grpc_tools.protoc -I=dc/protos --python_out=dc/generated --grpc_python_out=dc/generated dc/protos/dc.proto
python -m grpc_tools.protoc -I=dc/protos/dc.proto -I=dc/protos --python_out=dc/generated --grpc_python_out=dc/generated dc/protos/dclegacy.proto
python -m grpc_tools.protoc -I=dc/protos --python_out=dc/generated --grpc_python_out=dc/generated dc/protos/dcbase.proto
python -m grpc_tools.protoc -I=dc/protos --python_out=dc/generated --grpc_python_out=dc/generated dc/protos/dcmining.proto

# Patch import problem in generated code
sed -i 's|import dc_pb2 as dc__pb2|import dc.generated.dc_pb2 as dc__pb2|g' dc/generated/dc_pb2_grpc.py
sed -i 's|import dc_pb2 as dc__pb2|import dc.generated.dc_pb2 as dc__pb2|g' dc/generated/dclegacy_pb2.py
sed -i 's|import dc_pb2 as dc__pb2|import dc.generated.dc_pb2 as dc__pb2|g' dc/generated/dcmining_pb2.py

sed -i 's|import dclegacy_pb2 as dclegacy__pb2|import dc.generated.dclegacy_pb2 as dclegacy__pb2|g' dc/generated/dclegacy_pb2_grpc.py
sed -i 's|import dcbase_pb2 as dcbase__pb2|import dc.generated.dcbase_pb2 as dcbase__pb2|g' dc/generated/dcbase_pb2_grpc.py
sed -i 's|import dcmining_pb2 as dcmining__pb2|import dc.generated.dcmining_pb2 as dcmining__pb2|g' dc/generated/dcmining_pb2_grpc.py

find dc/generated -name '*.py'|grep -v migrations|xargs autoflake --in-place

#docker run --rm \
#  -v $(pwd)/docs/proto:/out \
#  -v $(pwd)/dc/protos:/protos \
#  pseudomuto/protoc-gen-doc --doc_opt=markdown,proto.md
#
#docker run --rm \
#  -v $(pwd)/docs/proto:/out \
#  -v $(pwd)/dc/protos:/protos \
#  pseudomuto/protoc-gen-doc --doc_opt=html,index.html

popd > /dev/null
