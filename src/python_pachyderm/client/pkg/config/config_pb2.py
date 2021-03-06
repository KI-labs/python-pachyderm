# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: client/pkg/config/config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='client/pkg/config/config.proto',
  package='config',
  syntax='proto3',
  serialized_options=_b('Z4github.com/pachyderm/pachyderm/src/client/pkg/config'),
  serialized_pb=_b('\n\x1e\x63lient/pkg/config/config.proto\x12\x06\x63onfig\"U\n\x06\x43onfig\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x1c\n\x02v1\x18\x02 \x01(\x0b\x32\x10.config.ConfigV1\x12\x1c\n\x02v2\x18\x03 \x01(\x0b\x32\x10.config.ConfigV2\"h\n\x08\x43onfigV1\x12\x15\n\rpachd_address\x18\x02 \x01(\t\x12\x12\n\nserver_cas\x18\x03 \x01(\t\x12\x15\n\rsession_token\x18\x01 \x01(\t\x12\x1a\n\x12\x61\x63tive_transaction\x18\x04 \x01(\t\"\xa7\x01\n\x08\x43onfigV2\x12\x16\n\x0e\x61\x63tive_context\x18\x01 \x01(\t\x12\x30\n\x08\x63ontexts\x18\x02 \x03(\x0b\x32\x1e.config.ConfigV2.ContextsEntry\x12\x0f\n\x07metrics\x18\x03 \x01(\x08\x1a@\n\rContextsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1e\n\x05value\x18\x02 \x01(\x0b\x32\x0f.config.Context:\x02\x38\x01\"\x8e\x01\n\x07\x43ontext\x12%\n\x06source\x18\x01 \x01(\x0e\x32\x15.config.ContextSource\x12\x15\n\rpachd_address\x18\x02 \x01(\t\x12\x12\n\nserver_cas\x18\x03 \x01(\t\x12\x15\n\rsession_token\x18\x04 \x01(\t\x12\x1a\n\x12\x61\x63tive_transaction\x18\x05 \x01(\t*(\n\rContextSource\x12\x08\n\x04NONE\x10\x00\x12\r\n\tCONFIG_V1\x10\x01\x42\x36Z4github.com/pachyderm/pachyderm/src/client/pkg/configb\x06proto3')
)

_CONTEXTSOURCE = _descriptor.EnumDescriptor(
  name='ContextSource',
  full_name='config.ContextSource',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONFIG_V1', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=550,
  serialized_end=590,
)
_sym_db.RegisterEnumDescriptor(_CONTEXTSOURCE)

ContextSource = enum_type_wrapper.EnumTypeWrapper(_CONTEXTSOURCE)
NONE = 0
CONFIG_V1 = 1



_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='config.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='config.Config.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='v1', full_name='config.Config.v1', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='v2', full_name='config.Config.v2', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=42,
  serialized_end=127,
)


_CONFIGV1 = _descriptor.Descriptor(
  name='ConfigV1',
  full_name='config.ConfigV1',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pachd_address', full_name='config.ConfigV1.pachd_address', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='server_cas', full_name='config.ConfigV1.server_cas', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='session_token', full_name='config.ConfigV1.session_token', index=2,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='active_transaction', full_name='config.ConfigV1.active_transaction', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=129,
  serialized_end=233,
)


_CONFIGV2_CONTEXTSENTRY = _descriptor.Descriptor(
  name='ContextsEntry',
  full_name='config.ConfigV2.ContextsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='config.ConfigV2.ContextsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='config.ConfigV2.ContextsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=339,
  serialized_end=403,
)

_CONFIGV2 = _descriptor.Descriptor(
  name='ConfigV2',
  full_name='config.ConfigV2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='active_context', full_name='config.ConfigV2.active_context', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contexts', full_name='config.ConfigV2.contexts', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metrics', full_name='config.ConfigV2.metrics', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CONFIGV2_CONTEXTSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=236,
  serialized_end=403,
)


_CONTEXT = _descriptor.Descriptor(
  name='Context',
  full_name='config.Context',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source', full_name='config.Context.source', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pachd_address', full_name='config.Context.pachd_address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='server_cas', full_name='config.Context.server_cas', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='session_token', full_name='config.Context.session_token', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='active_transaction', full_name='config.Context.active_transaction', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=406,
  serialized_end=548,
)

_CONFIG.fields_by_name['v1'].message_type = _CONFIGV1
_CONFIG.fields_by_name['v2'].message_type = _CONFIGV2
_CONFIGV2_CONTEXTSENTRY.fields_by_name['value'].message_type = _CONTEXT
_CONFIGV2_CONTEXTSENTRY.containing_type = _CONFIGV2
_CONFIGV2.fields_by_name['contexts'].message_type = _CONFIGV2_CONTEXTSENTRY
_CONTEXT.fields_by_name['source'].enum_type = _CONTEXTSOURCE
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
DESCRIPTOR.message_types_by_name['ConfigV1'] = _CONFIGV1
DESCRIPTOR.message_types_by_name['ConfigV2'] = _CONFIGV2
DESCRIPTOR.message_types_by_name['Context'] = _CONTEXT
DESCRIPTOR.enum_types_by_name['ContextSource'] = _CONTEXTSOURCE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), dict(
  DESCRIPTOR = _CONFIG,
  __module__ = 'client.pkg.config.config_pb2'
  # @@protoc_insertion_point(class_scope:config.Config)
  ))
_sym_db.RegisterMessage(Config)

ConfigV1 = _reflection.GeneratedProtocolMessageType('ConfigV1', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGV1,
  __module__ = 'client.pkg.config.config_pb2'
  # @@protoc_insertion_point(class_scope:config.ConfigV1)
  ))
_sym_db.RegisterMessage(ConfigV1)

ConfigV2 = _reflection.GeneratedProtocolMessageType('ConfigV2', (_message.Message,), dict(

  ContextsEntry = _reflection.GeneratedProtocolMessageType('ContextsEntry', (_message.Message,), dict(
    DESCRIPTOR = _CONFIGV2_CONTEXTSENTRY,
    __module__ = 'client.pkg.config.config_pb2'
    # @@protoc_insertion_point(class_scope:config.ConfigV2.ContextsEntry)
    ))
  ,
  DESCRIPTOR = _CONFIGV2,
  __module__ = 'client.pkg.config.config_pb2'
  # @@protoc_insertion_point(class_scope:config.ConfigV2)
  ))
_sym_db.RegisterMessage(ConfigV2)
_sym_db.RegisterMessage(ConfigV2.ContextsEntry)

Context = _reflection.GeneratedProtocolMessageType('Context', (_message.Message,), dict(
  DESCRIPTOR = _CONTEXT,
  __module__ = 'client.pkg.config.config_pb2'
  # @@protoc_insertion_point(class_scope:config.Context)
  ))
_sym_db.RegisterMessage(Context)


DESCRIPTOR._options = None
_CONFIGV2_CONTEXTSENTRY._options = None
# @@protoc_insertion_point(module_scope)
