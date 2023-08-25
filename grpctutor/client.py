# Copyright 2020 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python AsyncIO implementation of the GRPC hello.HelloService client."""

import asyncio
import logging
import os
import grpc
import sys
from grpctutor.services.hello.client import Hello

    
async def run(host, port, name) -> None:
    async with grpc.aio.insecure_channel(f"{host}:{port}") as channel:
        hello = Hello(channel)
        response = await hello.SayHello(name)
        print(response)

if __name__ == "__main__":
    host = os.environ.get('HELLO_SERVICE_HOST','[::]')
    port = os.environ.get('HELLO_SERVICE_PORT','50051')
    logging.basicConfig(level=logging.INFO)
    if len(sys.argv) < 2:
        print("Usage: python client.py <name>")
        sys.exit(1)
    
    asyncio.run(run(host, port, sys.argv[1]))