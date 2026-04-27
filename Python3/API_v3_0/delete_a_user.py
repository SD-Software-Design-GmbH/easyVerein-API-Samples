import requests

# First ask the user to enter the id of the user
user = input("Please enter the member ID: ")
if user.isdigit():
    # Add a access-token and hand over the delete request to the server
    header={'Authorization': 'Bearer <YOUR-API-KEY>'}
    request = requests.delete(f'https://easyverein.com/api/v3.0/member/{user}/', headers=header)
    print(request.headers)
    print(request.status_code)
else:
    print("Invalid member ID")
