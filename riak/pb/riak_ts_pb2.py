from six import *
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: riak_ts.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import riak.pb.riak_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='riak_ts.proto',
  package='',
  serialized_pb='\n\rriak_ts.proto\x1a\nriak.proto\"[\n\nTsQueryReq\x12\x1f\n\x05query\x18\x01 \x01(\x0b\x32\x10.TsInterpolation\x12\x15\n\x06stream\x18\x02 \x01(\x08:\x05\x66\x61lse\x12\x15\n\rcover_context\x18\x03 \x01(\x0c\"^\n\x0bTsQueryResp\x12%\n\x07\x63olumns\x18\x01 \x03(\x0b\x32\x14.TsColumnDescription\x12\x14\n\x04rows\x18\x02 \x03(\x0b\x32\x06.TsRow\x12\x12\n\x04\x64one\x18\x03 \x01(\x08:\x04true\"@\n\x08TsGetReq\x12\r\n\x05table\x18\x01 \x02(\x0c\x12\x14\n\x03key\x18\x02 \x03(\x0b\x32\x07.TsCell\x12\x0f\n\x07timeout\x18\x03 \x01(\r\"H\n\tTsGetResp\x12%\n\x07\x63olumns\x18\x01 \x03(\x0b\x32\x14.TsColumnDescription\x12\x14\n\x04rows\x18\x02 \x03(\x0b\x32\x06.TsRow\"V\n\x08TsPutReq\x12\r\n\x05table\x18\x01 \x02(\x0c\x12%\n\x07\x63olumns\x18\x02 \x03(\x0b\x32\x14.TsColumnDescription\x12\x14\n\x04rows\x18\x03 \x03(\x0b\x32\x06.TsRow\"\x0b\n\tTsPutResp\"P\n\x08TsDelReq\x12\r\n\x05table\x18\x01 \x02(\x0c\x12\x14\n\x03key\x18\x02 \x03(\x0b\x32\x07.TsCell\x12\x0e\n\x06vclock\x18\x03 \x01(\x0c\x12\x0f\n\x07timeout\x18\x04 \x01(\r\"\x0b\n\tTsDelResp\"A\n\x0fTsInterpolation\x12\x0c\n\x04\x62\x61se\x18\x01 \x02(\x0c\x12 \n\x0einterpolations\x18\x02 \x03(\x0b\x32\x08.RpbPair\"@\n\x13TsColumnDescription\x12\x0c\n\x04name\x18\x01 \x02(\x0c\x12\x1b\n\x04type\x18\x02 \x02(\x0e\x32\r.TsColumnType\"\x1f\n\x05TsRow\x12\x16\n\x05\x63\x65lls\x18\x01 \x03(\x0b\x32\x07.TsCell\"{\n\x06TsCell\x12\x15\n\rvarchar_value\x18\x01 \x01(\x0c\x12\x14\n\x0csint64_value\x18\x02 \x01(\x12\x12\x17\n\x0ftimestamp_value\x18\x03 \x01(\x12\x12\x15\n\rboolean_value\x18\x04 \x01(\x08\x12\x14\n\x0c\x64ouble_value\x18\x05 \x01(\x01\"/\n\rTsListKeysReq\x12\r\n\x05table\x18\x01 \x02(\x0c\x12\x0f\n\x07timeout\x18\x02 \x01(\r\"4\n\x0eTsListKeysResp\x12\x14\n\x04keys\x18\x01 \x03(\x0b\x32\x06.TsRow\x12\x0c\n\x04\x64one\x18\x02 \x01(\x08\"q\n\rTsCoverageReq\x12\x1f\n\x05query\x18\x01 \x01(\x0b\x32\x10.TsInterpolation\x12\r\n\x05table\x18\x02 \x02(\x0c\x12\x15\n\rreplace_cover\x18\x03 \x01(\x0c\x12\x19\n\x11unavailable_cover\x18\x04 \x03(\x0c\"3\n\x0eTsCoverageResp\x12!\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x10.TsCoverageEntry\"[\n\x0fTsCoverageEntry\x12\n\n\x02ip\x18\x01 \x02(\x0c\x12\x0c\n\x04port\x18\x02 \x02(\r\x12\x15\n\rcover_context\x18\x03 \x02(\x0c\x12\x17\n\x05range\x18\x04 \x01(\x0b\x32\x08.TsRange\"\x93\x01\n\x07TsRange\x12\x12\n\nfield_name\x18\x01 \x02(\x0c\x12\x13\n\x0blower_bound\x18\x02 \x02(\x12\x12\x1d\n\x15lower_bound_inclusive\x18\x03 \x02(\x08\x12\x13\n\x0bupper_bound\x18\x04 \x02(\x12\x12\x1d\n\x15upper_bound_inclusive\x18\x05 \x02(\x08\x12\x0c\n\x04\x64\x65sc\x18\x06 \x02(\x0c*Y\n\x0cTsColumnType\x12\x0b\n\x07VARCHAR\x10\x00\x12\n\n\x06SINT64\x10\x01\x12\n\n\x06\x44OUBLE\x10\x02\x12\r\n\tTIMESTAMP\x10\x03\x12\x0b\n\x07\x42OOLEAN\x10\x04\x12\x08\n\x04\x42LOB\x10\x05\x42#\n\x17\x63om.basho.riak.protobufB\x08RiakTsPB')

_TSCOLUMNTYPE = _descriptor.EnumDescriptor(
  name='TsColumnType',
  full_name='TsColumnType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='VARCHAR', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SINT64', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOUBLE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIMESTAMP', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOLEAN', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLOB', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1359,
  serialized_end=1448,
)

TsColumnType = enum_type_wrapper.EnumTypeWrapper(_TSCOLUMNTYPE)
VARCHAR = 0
SINT64 = 1
DOUBLE = 2
TIMESTAMP = 3
BOOLEAN = 4
BLOB = 5



_TSQUERYREQ = _descriptor.Descriptor(
  name='TsQueryReq',
  full_name='TsQueryReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='TsQueryReq.query', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stream', full_name='TsQueryReq.stream', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cover_context', full_name='TsQueryReq.cover_context', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
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
  extension_ranges=[],
  serialized_start=29,
  serialized_end=120,
)


_TSQUERYRESP = _descriptor.Descriptor(
  name='TsQueryResp',
  full_name='TsQueryResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='columns', full_name='TsQueryResp.columns', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rows', full_name='TsQueryResp.rows', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='done', full_name='TsQueryResp.done', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
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
  extension_ranges=[],
  serialized_start=122,
  serialized_end=216,
)


_TSGETREQ = _descriptor.Descriptor(
  name='TsGetReq',
  full_name='TsGetReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='table', full_name='TsGetReq.table', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key', full_name='TsGetReq.key', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='TsGetReq.timeout', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  extension_ranges=[],
  serialized_start=218,
  serialized_end=282,
)


_TSGETRESP = _descriptor.Descriptor(
  name='TsGetResp',
  full_name='TsGetResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='columns', full_name='TsGetResp.columns', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rows', full_name='TsGetResp.rows', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  extension_ranges=[],
  serialized_start=284,
  serialized_end=356,
)


_TSPUTREQ = _descriptor.Descriptor(
  name='TsPutReq',
  full_name='TsPutReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='table', full_name='TsPutReq.table', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='columns', full_name='TsPutReq.columns', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rows', full_name='TsPutReq.rows', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  extension_ranges=[],
  serialized_start=358,
  serialized_end=444,
)


_TSPUTRESP = _descriptor.Descriptor(
  name='TsPutResp',
  full_name='TsPutResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=446,
  serialized_end=457,
)


_TSDELREQ = _descriptor.Descriptor(
  name='TsDelReq',
  full_name='TsDelReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='table', full_name='TsDelReq.table', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key', full_name='TsDelReq.key', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vclock', full_name='TsDelReq.vclock', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='TsDelReq.timeout', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  extension_ranges=[],
  serialized_start=459,
  serialized_end=539,
)


_TSDELRESP = _descriptor.Descriptor(
  name='TsDelResp',
  full_name='TsDelResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=541,
  serialized_end=552,
)


_TSINTERPOLATION = _descriptor.Descriptor(
  name='TsInterpolation',
  full_name='TsInterpolation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='base', full_name='TsInterpolation.base', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='interpolations', full_name='TsInterpolation.interpolations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  extension_ranges=[],
  serialized_start=554,
  serialized_end=619,
)


_TSCOLUMNDESCRIPTION = _descriptor.Descriptor(
  name='TsColumnDescription',
  full_name='TsColumnDescription',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='TsColumnDescription.name', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='TsColumnDescription.type', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
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
  extension_ranges=[],
  serialized_start=621,
  serialized_end=685,
)


_TSROW = _descriptor.Descriptor(
  name='TsRow',
  full_name='TsRow',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cells', full_name='TsRow.cells', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  extension_ranges=[],
  serialized_start=687,
  serialized_end=718,
)


_TSCELL = _descriptor.Descriptor(
  name='TsCell',
  full_name='TsCell',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='varchar_value', full_name='TsCell.varchar_value', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sint64_value', full_name='TsCell.sint64_value', index=1,
      number=2, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp_value', full_name='TsCell.timestamp_value', index=2,
      number=3, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='boolean_value', full_name='TsCell.boolean_value', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='double_value', full_name='TsCell.double_value', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
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
  extension_ranges=[],
  serialized_start=720,
  serialized_end=843,
)


_TSLISTKEYSREQ = _descriptor.Descriptor(
  name='TsListKeysReq',
  full_name='TsListKeysReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='table', full_name='TsListKeysReq.table', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='TsListKeysReq.timeout', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  extension_ranges=[],
  serialized_start=845,
  serialized_end=892,
)


_TSLISTKEYSRESP = _descriptor.Descriptor(
  name='TsListKeysResp',
  full_name='TsListKeysResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keys', full_name='TsListKeysResp.keys', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='done', full_name='TsListKeysResp.done', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  extension_ranges=[],
  serialized_start=894,
  serialized_end=946,
)


_TSCOVERAGEREQ = _descriptor.Descriptor(
  name='TsCoverageReq',
  full_name='TsCoverageReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='TsCoverageReq.query', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='table', full_name='TsCoverageReq.table', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='replace_cover', full_name='TsCoverageReq.replace_cover', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unavailable_cover', full_name='TsCoverageReq.unavailable_cover', index=3,
      number=4, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  extension_ranges=[],
  serialized_start=948,
  serialized_end=1061,
)


_TSCOVERAGERESP = _descriptor.Descriptor(
  name='TsCoverageResp',
  full_name='TsCoverageResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entries', full_name='TsCoverageResp.entries', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  extension_ranges=[],
  serialized_start=1063,
  serialized_end=1114,
)


_TSCOVERAGEENTRY = _descriptor.Descriptor(
  name='TsCoverageEntry',
  full_name='TsCoverageEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip', full_name='TsCoverageEntry.ip', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port', full_name='TsCoverageEntry.port', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cover_context', full_name='TsCoverageEntry.cover_context', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='range', full_name='TsCoverageEntry.range', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  extension_ranges=[],
  serialized_start=1116,
  serialized_end=1207,
)


_TSRANGE = _descriptor.Descriptor(
  name='TsRange',
  full_name='TsRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='field_name', full_name='TsRange.field_name', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lower_bound', full_name='TsRange.lower_bound', index=1,
      number=2, type=18, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lower_bound_inclusive', full_name='TsRange.lower_bound_inclusive', index=2,
      number=3, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='upper_bound', full_name='TsRange.upper_bound', index=3,
      number=4, type=18, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='upper_bound_inclusive', full_name='TsRange.upper_bound_inclusive', index=4,
      number=5, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='desc', full_name='TsRange.desc', index=5,
      number=6, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
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
  extension_ranges=[],
  serialized_start=1210,
  serialized_end=1357,
)

_TSQUERYREQ.fields_by_name['query'].message_type = _TSINTERPOLATION
_TSQUERYRESP.fields_by_name['columns'].message_type = _TSCOLUMNDESCRIPTION
_TSQUERYRESP.fields_by_name['rows'].message_type = _TSROW
_TSGETREQ.fields_by_name['key'].message_type = _TSCELL
_TSGETRESP.fields_by_name['columns'].message_type = _TSCOLUMNDESCRIPTION
_TSGETRESP.fields_by_name['rows'].message_type = _TSROW
_TSPUTREQ.fields_by_name['columns'].message_type = _TSCOLUMNDESCRIPTION
_TSPUTREQ.fields_by_name['rows'].message_type = _TSROW
_TSDELREQ.fields_by_name['key'].message_type = _TSCELL
_TSINTERPOLATION.fields_by_name['interpolations'].message_type = riak.pb.riak_pb2._RPBPAIR
_TSCOLUMNDESCRIPTION.fields_by_name['type'].enum_type = _TSCOLUMNTYPE
_TSROW.fields_by_name['cells'].message_type = _TSCELL
_TSLISTKEYSRESP.fields_by_name['keys'].message_type = _TSROW
_TSCOVERAGEREQ.fields_by_name['query'].message_type = _TSINTERPOLATION
_TSCOVERAGERESP.fields_by_name['entries'].message_type = _TSCOVERAGEENTRY
_TSCOVERAGEENTRY.fields_by_name['range'].message_type = _TSRANGE
DESCRIPTOR.message_types_by_name['TsQueryReq'] = _TSQUERYREQ
DESCRIPTOR.message_types_by_name['TsQueryResp'] = _TSQUERYRESP
DESCRIPTOR.message_types_by_name['TsGetReq'] = _TSGETREQ
DESCRIPTOR.message_types_by_name['TsGetResp'] = _TSGETRESP
DESCRIPTOR.message_types_by_name['TsPutReq'] = _TSPUTREQ
DESCRIPTOR.message_types_by_name['TsPutResp'] = _TSPUTRESP
DESCRIPTOR.message_types_by_name['TsDelReq'] = _TSDELREQ
DESCRIPTOR.message_types_by_name['TsDelResp'] = _TSDELRESP
DESCRIPTOR.message_types_by_name['TsInterpolation'] = _TSINTERPOLATION
DESCRIPTOR.message_types_by_name['TsColumnDescription'] = _TSCOLUMNDESCRIPTION
DESCRIPTOR.message_types_by_name['TsRow'] = _TSROW
DESCRIPTOR.message_types_by_name['TsCell'] = _TSCELL
DESCRIPTOR.message_types_by_name['TsListKeysReq'] = _TSLISTKEYSREQ
DESCRIPTOR.message_types_by_name['TsListKeysResp'] = _TSLISTKEYSRESP
DESCRIPTOR.message_types_by_name['TsCoverageReq'] = _TSCOVERAGEREQ
DESCRIPTOR.message_types_by_name['TsCoverageResp'] = _TSCOVERAGERESP
DESCRIPTOR.message_types_by_name['TsCoverageEntry'] = _TSCOVERAGEENTRY
DESCRIPTOR.message_types_by_name['TsRange'] = _TSRANGE

@add_metaclass(_reflection.GeneratedProtocolMessageType)
class TsQueryReq(_message.Message):
  DESCRIPTOR = _TSQUERYREQ

  # @@protoc_insertion_point(class_scope:TsQueryReq)

@add_metaclass(_reflection.GeneratedProtocolMessageType)
class TsQueryResp(_message.Message):
  DESCRIPTOR = _TSQUERYRESP

  # @@protoc_insertion_point(class_scope:TsQueryResp)

@add_metaclass(_reflection.GeneratedProtocolMessageType)
class TsGetReq(_message.Message):
  DESCRIPTOR = _TSGETREQ

  # @@protoc_insertion_point(class_scope:TsGetReq)

@add_metaclass(_reflection.GeneratedProtocolMessageType)
class TsGetResp(_message.Message):
  DESCRIPTOR = _TSGETRESP

  # @@protoc_insertion_point(class_scope:TsGetResp)

@add_metaclass(_reflection.GeneratedProtocolMessageType)
class TsPutReq(_message.Message):
  DESCRIPTOR = _TSPUTREQ

  # @@protoc_insertion_point(class_scope:TsPutReq)

@add_metaclass(_reflection.GeneratedProtocolMessageType)
class TsPutResp(_message.Message):
  DESCRIPTOR = _TSPUTRESP

  # @@protoc_insertion_point(class_scope:TsPutResp)

@add_metaclass(_reflection.GeneratedProtocolMessageType)
class TsDelReq(_message.Message):
  DESCRIPTOR = _TSDELREQ

  # @@protoc_insertion_point(class_scope:TsDelReq)

@add_metaclass(_reflection.GeneratedProtocolMessageType)
class TsDelResp(_message.Message):
  DESCRIPTOR = _TSDELRESP

  # @@protoc_insertion_point(class_scope:TsDelResp)

@add_metaclass(_reflection.GeneratedProtocolMessageType)
class TsInterpolation(_message.Message):
  DESCRIPTOR = _TSINTERPOLATION

  # @@protoc_insertion_point(class_scope:TsInterpolation)

@add_metaclass(_reflection.GeneratedProtocolMessageType)
class TsColumnDescription(_message.Message):
  DESCRIPTOR = _TSCOLUMNDESCRIPTION

  # @@protoc_insertion_point(class_scope:TsColumnDescription)

@add_metaclass(_reflection.GeneratedProtocolMessageType)
class TsRow(_message.Message):
  DESCRIPTOR = _TSROW

  # @@protoc_insertion_point(class_scope:TsRow)

@add_metaclass(_reflection.GeneratedProtocolMessageType)
class TsCell(_message.Message):
  DESCRIPTOR = _TSCELL

  # @@protoc_insertion_point(class_scope:TsCell)

@add_metaclass(_reflection.GeneratedProtocolMessageType)
class TsListKeysReq(_message.Message):
  DESCRIPTOR = _TSLISTKEYSREQ

  # @@protoc_insertion_point(class_scope:TsListKeysReq)

@add_metaclass(_reflection.GeneratedProtocolMessageType)
class TsListKeysResp(_message.Message):
  DESCRIPTOR = _TSLISTKEYSRESP

  # @@protoc_insertion_point(class_scope:TsListKeysResp)

@add_metaclass(_reflection.GeneratedProtocolMessageType)
class TsCoverageReq(_message.Message):
  DESCRIPTOR = _TSCOVERAGEREQ

  # @@protoc_insertion_point(class_scope:TsCoverageReq)

@add_metaclass(_reflection.GeneratedProtocolMessageType)
class TsCoverageResp(_message.Message):
  DESCRIPTOR = _TSCOVERAGERESP

  # @@protoc_insertion_point(class_scope:TsCoverageResp)

@add_metaclass(_reflection.GeneratedProtocolMessageType)
class TsCoverageEntry(_message.Message):
  DESCRIPTOR = _TSCOVERAGEENTRY

  # @@protoc_insertion_point(class_scope:TsCoverageEntry)

@add_metaclass(_reflection.GeneratedProtocolMessageType)
class TsRange(_message.Message):
  DESCRIPTOR = _TSRANGE

  # @@protoc_insertion_point(class_scope:TsRange)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\027com.basho.riak.protobufB\010RiakTsPB')
# @@protoc_insertion_point(module_scope)
