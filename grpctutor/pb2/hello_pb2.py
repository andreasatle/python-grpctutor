# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hello.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bhello.proto\x12\x05hello\"\x1f\n\x0fSayHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"#\n\x10SayHelloResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2F\n\x05Hello\x12=\n\x08SayHello\x12\x16.hello.SayHelloRequest\x1a\x17.hello.SayHelloResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'hello_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SAYHELLOREQUEST._serialized_start=22
  _SAYHELLOREQUEST._serialized_end=53
  _SAYHELLORESPONSE._serialized_start=55
  _SAYHELLORESPONSE._serialized_end=90
  _HELLO._serialized_start=92
  _HELLO._serialized_end=162
# @@protoc_insertion_point(module_scope)