# First ask the user to enter a path to a json
read -p "Please give me the path to the JSON: " thejson

# Check if the given file exists
if ! test -f "$thejson"; then
    echo "The file does not exist!"
    exit
fi

# If all given values are valid, start the transfer
curl -X POST https://easyverein.com/api/stable/member/ -H 'Authorization: Bearer <YOUR-API-KEY>
Content-Type: application/json' -d @$thejson
