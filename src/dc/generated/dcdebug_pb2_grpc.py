# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import dc.generated.dcdebug_pb2 as dcdebug__pb2


class DebugAPIStub(object):
  """//////////////////////////
  //////////////////////////
  //////////////////////////
  ////     API       ///////
  //////////////////////////
  //////////////////////////
  //////////////////////////

  This service describes the Debug API used for debugging
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetFullState = channel.unary_unary(
        '/dc.DebugAPI/GetFullState',
        request_serializer=dcdebug__pb2.GetFullStateReq.SerializeToString,
        response_deserializer=dcdebug__pb2.GetFullStateResp.FromString,
        )


class DebugAPIServicer(object):
  """//////////////////////////
  //////////////////////////
  //////////////////////////
  ////     API       ///////
  //////////////////////////
  //////////////////////////
  //////////////////////////

  This service describes the Debug API used for debugging
  """

  def GetFullState(self, request, context):
    # missing associated documentation comment in .proto file
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DebugAPIServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetFullState': grpc.unary_unary_rpc_method_handler(
          servicer.GetFullState,
          request_deserializer=dcdebug__pb2.GetFullStateReq.FromString,
          response_serializer=dcdebug__pb2.GetFullStateResp.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'dc.DebugAPI', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))