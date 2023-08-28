<?php
//require 'vendor/autoload.php';

use Illuminate\Support\Facades\Log;
use Illuminate\Support\Facades\Route;
use Hello\HelloClient;
use Hello\SayHelloRequest;

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

$client = new HelloClient('[::]:50051', [
    'credentials' => Grpc\ChannelCredentials::createInsecure(),
]);

Route::get('/', function () {
    return view('welcome');
});

Route::get('/name/{name}', function ($name) use ($client) {
    $request = new SayHelloRequest();
    $request->setName($name);
    list($response, $status) = $client->SayHello($request)->wait();
    Log::info($response->getMessage());
    return $response->getMessage();
});