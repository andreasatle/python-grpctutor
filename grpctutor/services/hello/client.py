from grpctutor.pb2 import hello_pb2, hello_pb2_grpc
import logging

class Hello:
    def __init__(self, channel):
        self.stub = hello_pb2_grpc.HelloStub(channel)

    async def SayHello(self, name):
        request = hello_pb2.SayHelloRequest(name=name)
        response = await self.stub.SayHello(request)
        logging.info(f"rpc SayHello(name=\'{request.name}\') => message=\'{response.message}\'")
        return response.message
