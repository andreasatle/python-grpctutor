import asyncio
import logging
import os
import grpc

# Import the generated classes
from grpctutor.services.hello.service import Hello


async def serve():
    # Create a new server
    server = grpc.aio.server()

    # Add the Hello Service to the server
    Hello.add_to_server(server)

    # Listen on port
    #listen_addr = f"{host}:{port}"
    listen_addr = f"[::]:50051"

    # Start the server
    server.add_insecure_port(listen_addr)

    # Logging
    logging.info(f"Starting server on {listen_addr}")

    # Start the server
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())
