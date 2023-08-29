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

## Generate PHP-files with Docker
In the `protos` directory, run `protoc-all` with docker:
```bash
docker run -v $PWD:/defs namely/protoc-all -f hello.proto -l php
```
This will create a directory `gen/pb-php` containing the generated PHP files.

# Docker
In the project root-directory, there is a Docker file.
In this directory, build a Docker image with:
```bash
docker build -t python-grpctutor-server .
```
The server can be started with:
```bash
docker run -p 50051:50051 python-grpctutor-server
```

# gRPC-client for PHP
Using `pecl`, we can install `gRPC` by
```bash
pecl install grpc
```

Create your `PHP`/`laravel` project by:
```bash
composer create-project --prefer-dist laravel/laravel laravel-webserver
```
and add some requirements
```bash
composer require google/protobuf
composer require grpc/grpc
```

We need to add a few lines in the `composer.json` file:
```bash
    "autoload": {
        "psr-4": {
            ...
            "Hello\\": "../protos/gen/pb-php/Hello",
            "GPBMetadata\\": "../protos/gen/pb-php/GPBMetadata"
        }
    },
```

The `routes/web.php` is modified:
```php
<?php

use Hello\HelloClient;
use Hello\SayHelloRequest;

use Illuminate\Support\Facades\Route;

$client = new HelloClient('localhost:50051', [
    'credentials' => Grpc\ChannelCredentials::createInsecure(),
]);

Route::get('/name/{name}', function ($name) use ($client) {
    $request = new SayHelloRequest();
    $request->setName($name);
    list($reply, $status) = $client->SayHello($request)->wait();
    return $reply->getMessage();
});
```