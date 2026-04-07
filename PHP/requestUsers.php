<?php

# Set the API version
$apiVersion = 'stable'

# Creating the header with the Token in it
$opts = [
    "http" => [
        "method" => "GET",
        "header" => "Authorization: Bearer <YOUR-API-KEY>"
    ]
];
$context = stream_context_create($opts);
# Execute the request
$content = file_get_contents('https://easyverein.com/api/' . $apiVersion . '/member/', false, $context);

# Decode the JSON and get the count value from it
$json = json_decode($content);
echo $json->count;

?>
