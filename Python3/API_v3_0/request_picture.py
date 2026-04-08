# Because there are some questions about how to request a file (like the profile_picture) here is an example for such a request

import requests


header={
    'Authorization': 'Bearer <YOUR-API-KEY>',
    'Accept': 'application/json, image/*'
}

# Get the entries as json from the server
res = requests.get('https://easyverein.com/api/v3.0/member/', headers=header)

# Extract the first entry of the responded entries
all_entries = res.json()
some_entry = all_entries.get('results')[0]

# get the url of the profile picture
url = some_entry.get('profile_picture')
print(url)

# Get the image
image = requests.get(url, headers=header, stream=True)

# The raw image, write it to a file to use it
print(image)
