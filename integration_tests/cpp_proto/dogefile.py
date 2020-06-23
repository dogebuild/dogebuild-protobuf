from pathlib import Path
from dogebuild_protobuf import proto_mode, ProtobufPlugin

proto_mode()

ProtobufPlugin(src=Path("src").glob("**/*.proto"),)
