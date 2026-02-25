import requests

header={
    'Authorization': 'Bearer <YOUR-API-KEY>',
    'Content-Disposition': 'name="file"; filename="file.png"'
}

# The files must be a dictionary with the key of the field of the picture
files = {'_profilePicture': open('/path/to/your/file.png', 'rb+')}

url = 'https://easyverein.com/api/stable/member/1/'
response = requests.patch(url, files=files, headers=header)
print(response.status_code)
print(response.json())
