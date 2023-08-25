# Import the generated classes
from grpctutor.pb2 import hello_pb2, hello_pb2_grpc
import logging

# Implementation of the Hello Service
class Hello(hello_pb2_grpc.HelloServicer):
    # Utility method, to hide the complexity of adding the service to a server
    @staticmethod
    def add_to_server(server):
        hello_pb2_grpc.add_HelloServicer_to_server(Hello(), server)

    async def SayHello(self, request, context):
        message = f"Hello, {request.name}!"
        logging.info(f"rpc SayHello(name=\'{request.name}\')")
        response = hello_pb2.SayHelloResponse(message=message)
        return response

