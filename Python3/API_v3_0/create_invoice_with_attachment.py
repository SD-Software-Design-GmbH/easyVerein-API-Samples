import requests

header={
    'Authorization': 'Bearer <YOUR-API-KEY>',
}

# First create an invoice that is editable
data = {
    'inv_number': 123,
    'receiver': 'someone',
    'total_price': 13.37,
    'is_draft': True # This is needed to patch the file later for the invoice
}

url = 'https://easyverein.com/api/v3.0/invoice'
response = requests.post(url, json=data, headers=header)
invoice_id = response.json().get('id')
url = f'{url}/{invoice_id}'

header['Content-Disposition'] = 'name="file"; filename="file.pdf"'

# The file can be a picture or a pdf
files = {'path': open('/path/to/your/file.pdf', 'rb+')}
response = requests.patch(url, files=files, headers=header)

# Set the invoice to be no draft - The invoice cannot be changed after this step
data = {
    'is_draft': False
}

response = requests.patch(url, json=data, headers=header)

print(response)
