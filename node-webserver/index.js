// Import required modules
const express = require('express');
const grpc = require("@grpc/grpc-js");
const protoLoader = require("@grpc/proto-loader");

// Path to protobuf file
const PROTO_PATH = "../protos/hello.proto";

const host = process.env.GRPCTUTOR_HELLO_SERVICE_HOST || "127.0.0.1";
// Some options for the protobuf loader
const options = {
    keepCase: true,
    longs: String,
    enums: String,
    defaults: true,
    oneofs: true,
};

const packageDefinition = protoLoader.loadSync(PROTO_PATH, options);

const hello_proto = grpc.loadPackageDefinition(packageDefinition).hello;
const client = new hello_proto.Hello(
    `${host}:50051`,
    grpc.credentials.createInsecure()
);

// Define gRPC client
async function pingPongName(req, res) {
    client.sayHello({ name: req.params.name }, function (err, response) {
        if (err) {
            res.send('rpc sayHello, error: ' + err.details + ', Error code: ' + err.code)
            return
        }
        console.log('Node Server rpc sayHello(', req.params, ')')
        res.send(response.message + '\n');
    });
}

// Create an Express application
const app = express();

// Define a route
app.get('/name/:name', pingPongName);

// Start the server
const port = process.env.PORT || 3000;
app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
