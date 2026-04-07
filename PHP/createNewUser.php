<?php

# Set the API version
$apiVersion = 'stable'

# First ask the user to enter a path to a json and the id of the user
$input = readline("Enter the path to a JSON: ");
$file = fopen("$input", "r") or die("Don't tell me a lie!");
$data = fread($file, filesize("$input"));
fclose($file);

# Creating the header with the Token in it
$opts = [
    "http" => [
        "method" => "POST",
        "header" => "Authorization: Bearer <YOUR-API-KEY>\r\n" .
                    "Content-Type: application/json\r\n",
        "content" => $data
    ]
];
$context = stream_context_create($opts);
# Execute the request
$content = file_get_contents('https://easyverein.com/api/' . $apiVersion . '/member/', false, $context);
echo $content->http_response_code;
?>
