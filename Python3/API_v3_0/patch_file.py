import requests

header={
    'Authorization': 'Bearer <YOUR-API-KEY>',
    'Content-Disposition': 'name="file"; filename="file.png"'
}

# The files must be a dictionary with the key of the field of the picture
files = {'profile_picture': open('/path/to/your/file.png', 'rb+')}

# First ask the user to enter the id of the user
user = input("Please enter the member ID: ")

url = f'https://easyverein.com/api/v3.0/member/{user}/'
response = requests.patch(url, files=files, headers=header)
print(response.status_code)
print(response.json())