# Because there are some questions about how to request a file (like the _profilePicture) here is an example for such a request

import requests

# Get the entries as json from the server
header={
    'Authorization': 'Bearer <YOUR-API-KEY>',
    'Accept': 'application/json, image/*'
}
res = requests.get('https://easyverein.com/api/stable/member/', headers=header)

# Extract the first entry of the responded entries
allEntries = res.json()
someEntry = allEntries.get('results')[0]

# get the url of the profilePicture
url = someEntry.get('_profilePicture')
print(url)

# Get the image
image = requests.get(url, headers=header, stream=True)

# The raw image, write it to a file to use it
print(image)
