import asyncio
import logging
import os
import grpc

# Import the generated classes
from grpctutor.services import Hello


async def serve(host, port):
    # Create a new server
    server = grpc.aio.server()

    # Add the Hello Service to the server
    Hello.add_to_server(server)

    # Listen on port
    listen_addr = f"{host}:{port}"

    # Start the server
    server.add_insecure_port(listen_addr)

    # Logging
    logging.info(f"Starting server on {listen_addr}")

    # Start the server
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    host = os.environ.get('HELLO_SERVICE_HOST','[::]')
    port = os.environ.get('HELLO_SERVICE_PORT','50051')
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve(host, port))
