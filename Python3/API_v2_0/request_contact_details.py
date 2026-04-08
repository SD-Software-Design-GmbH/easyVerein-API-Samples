import requests


header={'Authorization': 'Bearer <YOUR-API-KEY>'}

# Get the entries as json from the server
res = requests.get('https://easyverein.com/api/v2.0/contact-details/?showCount=true', headers=header)

# Count the entries
count = res.json()
print(count["count"])
