import requests

header={
    'Authorization': 'Bearer <YOUR-API-KEY>',
}

# First create an invoice that is editable
data = {
    'invNumber': 123,
    'receiver': 'someone',
    'totalPrice': 13.37,
    'isDraft': True # This is needed to patch the file later for the invoice
}

url = 'https://easyverein.com/api/v1.4/invoice'
response = requests.post(url, json=data, headers=header)
invoiceId = response.json().get('id')
url = f'{url}/{invoiceId}'

header['Content-Disposition'] = 'name="file"; filename="file.pdf"'

# The file can be a picture or a pdf
files = {'path': open('/path/to/your/file.pdf', 'rb+')}
response = requests.patch(url, files=files, headers=header)

# Set the invoice to be no draft - The invoice cannot be changed after this step
data = {
    'isDraft': False
}

response = requests.patch(url, json=data, headers=header)

print(response)
