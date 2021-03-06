from pathlib import Path

from dogebuild import dependencies, doge, directory
from dogebuild_protobuf import proto_mode, ProtobufPlugin, DockerProtocBinary

proto_mode()

dependencies(doge(directory("../dependency"), tasks=["proto-sources"],))

ProtobufPlugin(src=Path("src").glob("**/*.proto"), protoc_binary=DockerProtocBinary('znly/protoc'))
