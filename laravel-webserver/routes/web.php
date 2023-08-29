<?php

use Hello\HelloClient;
use Hello\SayHelloRequest;

use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "web" middleware group. Make something great!
|
*/

$client = new HelloClient('localhost:50051', [
    'credentials' => Grpc\ChannelCredentials::createInsecure(),
]);



Route::get('/name/{name}', function ($name) use ($client) {
    $request = new SayHelloRequest();
    $request->setName($name);
    list($reply, $status) = $client->SayHello($request)->wait();
    return $reply->getMessage();
});