from .src.openapi_pb2_grpc import OpenapiServicer, add_OpenapiServicer_to_server


class OtgService(OpenapiServicer):
    def __init__(self, grpc_server):
        add_OpenapiServicer_to_server(self, grpc_server)

    def SetConfig(self, request, content):
        pass

