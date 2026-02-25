# Look how many enties are in the APIs JSON
curl -X GET https://easyverein.com/api/stable/contact-details/ -H 'Authorization: Bearer <YOUR-API-KEY>' | jq .'count'
