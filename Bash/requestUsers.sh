# Look how many enties are in the APIs JSON
curl -X GET https://easyverein.com/api/stable/member/ -H 'Authorization: Bearer <YOUR-API-KEY>' | jq .'count'
