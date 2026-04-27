import json
import requests

# First ask the user to enter a path to a json and the id of the user
file = input("Enter the path to a JSON: ")
user = input("Please enter the member ID: ")
if file.endswith(".json") and user.isdigit():
    try:
        with open(file, 'r') as json_file_data:
            raw_data = json_file_data.read()
            data = json.loads(raw_data)
    except FileNotFoundError:
        print("Don't tell me a lie!")
        quit()
    except IOError:
        print("I have decided and I want to die!")
        quit()
    except json.decoder.JSONDecodeError:
        print("Bah, I dont like that kind of file!")
        quit()
    # Add a access-token and hand over the json to the server
    header={'Authorization': 'Bearer <YOUR-API-KEY>'}
    request = requests.patch(f'https://easyverein.com/api/v3.0/member/{user}/', headers=header, json=data)
    print(request.headers)
    print(request.status_code)
elif user.isdigit():
    print("Well, you need to give me a json!")
else:
    print("Invalid member ID")
