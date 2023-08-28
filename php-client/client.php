<?php
require 'vendor/autoload.php';

use Hello\HelloClient;
use Hello\SayHelloRequest;

$client = new HelloClient('localhost:50051', [
    'credentials' => Grpc\ChannelCredentials::createInsecure(),
]);

$request = new SayHelloRequest();
$request->setName('Andreas');

list($response, $status) = $client->SayHello($request)->wait();

if ($status->code === Grpc\STATUS_OK) {
    echo "Response: " . $response->getMessage() . "\n";
} else {
    echo "RPC failed with status: " . $status->details . "\n";
}