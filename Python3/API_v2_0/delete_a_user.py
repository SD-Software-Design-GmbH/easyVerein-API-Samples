import requests

# Method to figure out if the given value is a integer or an integer as a string
def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return True

# First ask the user to enter the id of the user
user = input("Please enter the member ID: ")
if is_integer(user):
    # Add a access-token and hand over the delete request to the server
    header={'Authorization': 'Bearer <YOUR-API-KEY>'}
    request = requests.delete(f'https://easyverein.com/api/stable/member/{user}/', headers=header)
    print(request.headers)
    print(request.status_code)
else:
    print("You gave me a wrong ID")
