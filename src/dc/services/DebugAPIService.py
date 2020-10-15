# coding=utf-8
# Distributed under the MIT software license, see the accompanying
# file LICENSE or http://www.opensource.org/licenses/mit-license.php.
from dc.core import config
from dc.core.dcnode import dcNode
from dc.generated import dcdebug_pb2
from dc.generated.dcdebug_pb2_grpc import DebugAPIServicer
from dc.services.grpcHelper import GrpcExceptionWrapper


class DebugAPIService(DebugAPIServicer):
    MAX_REQUEST_QUANTITY = 100

    def __init__(self, dcnode: dcNode):
        self.dcnode = dcnode

    @GrpcExceptionWrapper(dcdebug_pb2.GetFullStateResp)
    def GetFullState(self, request: dcdebug_pb2.GetFullStateReq, context) -> dcdebug_pb2.GetFullStateResp:
        return dcdebug_pb2.GetFullStateResp(
            coinbase_state=self.dcnode.get_address_state(config.dev.coinbase_address).pbdata,
            addresses_state=self.dcnode.get_all_address_state()
        )
