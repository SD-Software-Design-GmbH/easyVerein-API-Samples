<?php

# First ask the user to enter the id of the user
$theID = readline("Please enter the member ID: ");
if (!is_numeric($theID)) {
    die("You gave me a wrong ID");
}

# Creating the header with the Token in it
$opts = [
    "http" => [
        "method" => "DELETE",
        "header" => "Authorization: Bearer <YOUR-API-KEY>\r\n"
    ]
];
$context = stream_context_create($opts);
# Execute the request
$content = file_get_contents('https://easyverein.com/api/stable/member/' . $theID . '/', false, $context);
?>
