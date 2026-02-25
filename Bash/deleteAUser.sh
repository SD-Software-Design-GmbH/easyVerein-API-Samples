# First ask the user to enter the id of the user
read -p "Please give me the ID of the member you want to delete: " theID

# Check if the given value is an integer
con='^[0-9]+([.][0-9]+)?$'
if ! [[ $theID =~ $con ]]; then
    echo "The given ID is invalid!"
    exit
fi

# If all given values are valid, start the transfer
curl -X DELETE https://easyverein.com/api/stable/member/$theID/ -H 'Authorization: Bearer <YOUR-API-KEY>'
