import requests

# Get the entries as json from the server
header={'Authorization': 'Bearer <YOUR-API-KEY>'}
res = requests.get('https://easyverein.com/api/stable/contact-details/', headers=header)

# Count the entries
count = res.json()
print(count["count"])
