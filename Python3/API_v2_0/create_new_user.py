import json
import requests


# First ask the user to enter a path to a json
file = input("Enter the path to a JSON:")
if file.endswith(".js"):
    try:
        # Try to open the given file, extract the data and check if the given file is a valid json
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
    print("The given file seems to be valid, doing the transfer...")
    header={'Authorization': 'Bearer <YOUR-API-KEY>'}
    request = requests.post('https://easyverein.com/api/v2.0/member/', headers=header, json=data)
    print(request.status_code)
else:
    print("Well, you need to give me a json!")
