import requests

# Get the entries as json from the server
header={'Authorization': 'Bearer <YOUR-API-KEY>'}
res = requests.get('https://easyverein.com/api/stable/member/', headers=header)

# count the entries
count = res.json()
print(count["count"])
