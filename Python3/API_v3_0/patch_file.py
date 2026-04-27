import requests

header={
    'Authorization': 'Bearer <YOUR-API-KEY>',
    'Content-Disposition': 'name="file"; filename="file.png"'
}

# The files must be a dictionary with the key of the field of the picture
with open('/path/to/your/file.png', 'rb+') as file_to_upload:
    files = {'profile_picture': file_to_upload}

    # First ask for the id of the user to change the profile picture for
    user = input("Please enter the member ID: ")

    url = f'https://easyverein.com/api/v3.0/member/{user}/'
    response = requests.patch(url, files=files, headers=header)
    print(response.status_code)
    print(response.json())
