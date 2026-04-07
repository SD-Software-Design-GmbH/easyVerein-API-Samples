# In newer versions (v1.5) of the api some endpoints like the /member/{userPk}/custom-fields can be used with a bulk-create and bulk-update
# For further information and to check which endpoints are enabled for the bulk actions see the documentation (https://easyverein.com/api/)

import requests

header={
    'Authorization': 'Bearer <YOUR-API-KEY>'
}

data = {
    'entries': [
        # Inside the entries list, the entries are nothing more like a normal post/patch body for the specific endpoint
        {
            'custom_field': 53851,
            'value': 'Linuxmasterrace'
        },
        {
            'custom_field': 53852,
            'value': 'I like trains'
        }
    ]
}

# First ask the user to enter the id of the user
user = input("Please enter the member ID: ")

# Assuming that the member already exist
response = requests.post(f'https://easyverein.com/api/latest/member/{user}/custom-fields/bulk-create', json=data, headers=header)

assert response.status_code == 200
