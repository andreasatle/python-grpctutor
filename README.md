# gRPC tutorial

## Create a `hello.proto` file
```python
syntax = "proto3";
package hello;

service Hello {
    rpc SayHello(SayHelloRequest) returns (SayHelloResponse) {}
}

message SayHelloRequest {
    string name = 1;
}

message SayHelloResponse {
    string message = 1;
}
```

## Install `grpcio-tools`
With `poetry` you write
```bash
poetry add grpcio-tools
```

## Generate python-files with docker
In the `protos` directory, run `protoc-all` with docker:
```bash
docker run -v $PWD:/defs namely/protoc-all -f hello.proto -l python
```
This will create a directory `gen/pb_python` containing the generated python files.

Those files are copied into `grpctutor/pb2`.

At last I have to change one import in `hello_pb2_grpc.py`,
```python
import grpctutor.pb2.hello_pb2 as hello__pb2
```


# gRPC-client for PHP
Using `pecl`, we can install `gRPC` by
```bash
pecl install gRPC
```

Create your `PHP`/`laravel` project by:
```bash
composer create-project --prefer-dist laravel/laravel grpctutor
```
and add some requirements
```bash
composer require google/protobuf
composer require grpc/grpc
composer req ext-grpc
```