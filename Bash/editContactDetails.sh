# First ask the user to enter a path to a json
read -p "Please give me the path to the JSON: " thejson

# Check if the given file exists
if ! test -f "$thejson"; then
    echo "The file does not exist!"
    exit
fi

# Than ask the user to enter the id of the user
read -p "Please give me the ID of the member you want to edit: " theID

# Check if the given value is an integer
con='^[0-9]+([.][0-9]+)?$'
if ! [[ $theID =~ $con ]]; then
    echo "The given ID is invalid!"
    exit
fi

# If all given values are valid, start the transfer
curl -X PATCH https://easyverein.com/api/stable/contact-details/$theID/ -H 'Authorization: Bearer <YOUR-API-KEY>
Content-Type: application/json' -d @$thejson
