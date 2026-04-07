import requests


header={'Authorization': 'Bearer <YOUR-API-KEY>'}

# Get the entries as json from the server
res = requests.get('https://easyverein.com/api/stable/member/?showCount=true', headers=header)

# count the entries
count = res.json()
print(count["count"])
