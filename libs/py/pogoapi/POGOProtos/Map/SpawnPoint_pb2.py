# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Map/SpawnPoint.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos/Map/SpawnPoint.proto',
  package='POGOProtos.Map',
  syntax='proto3',
  serialized_pb=_b('\n\x1fPOGOProtos/Map/SpawnPoint.proto\x12\x0ePOGOProtos.Map\"1\n\nSpawnPoint\x12\x10\n\x08latitude\x18\x02 \x01(\x01\x12\x11\n\tlongitude\x18\x03 \x01(\x01\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SPAWNPOINT = _descriptor.Descriptor(
  name='SpawnPoint',
  full_name='POGOProtos.Map.SpawnPoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='latitude', full_name='POGOProtos.Map.SpawnPoint.latitude', index=0,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='POGOProtos.Map.SpawnPoint.longitude', index=1,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=51,
  serialized_end=100,
)

DESCRIPTOR.message_types_by_name['SpawnPoint'] = _SPAWNPOINT

SpawnPoint = _reflection.GeneratedProtocolMessageType('SpawnPoint', (_message.Message,), dict(
  DESCRIPTOR = _SPAWNPOINT,
  __module__ = 'POGOProtos.Map.SpawnPoint_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Map.SpawnPoint)
  ))
_sym_db.RegisterMessage(SpawnPoint)


# @@protoc_insertion_point(module_scope)