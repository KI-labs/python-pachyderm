# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from python_pachyderm.client.version.versionpb import version_pb2 as client_dot_version_dot_versionpb_dot_version__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class APIStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetVersion = channel.unary_unary(
        '/versionpb.API/GetVersion',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=client_dot_version_dot_versionpb_dot_version__pb2.Version.FromString,
        )


class APIServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetVersion(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_APIServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetVersion': grpc.unary_unary_rpc_method_handler(
          servicer.GetVersion,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=client_dot_version_dot_versionpb_dot_version__pb2.Version.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'versionpb.API', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
