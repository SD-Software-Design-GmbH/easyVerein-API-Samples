import requests


header={'Authorization': 'Bearer <YOUR-API-KEY>'}

# Request members
nested_member_requests = [
    '{id,contactDetails{id,name},org{id,name,short},email,membershipNumber}',
    '{id,email,paymentAmount,customFields{id,org{id,short},userObject,customField{name},value}}'
]

# Request contact-details
nested_contact_details_requests = [
    '{id,org,name,age,customFields{id,value}}',
    '{id,customFields{addressObject{customFields{addressObject{id}}}}}'
]

response = [None] * 2
# Get the entries as json from the server
for nested_member_request, nested_contact_details_request in zip(nested_member_requests, nested_contact_details_requests):
    response[0] = requests.get('https://easyverein.com/api/stable/member?query={query}'.format(query=nested_member_request), headers=header)
    response[1] = requests.get('https://easyverein.com/api/stable/contact-details?query={query}'.format(query=nested_contact_details_request), headers=header)

    for res in response:
        if res.status_code == 200 and len(res.content) < 500:
            print(res.content)
        else:
            print(res.status_code)
