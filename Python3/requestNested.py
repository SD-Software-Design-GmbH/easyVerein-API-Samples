import requests

header={'Authorization': 'Bearer <YOUR-API-KEY>'}
version = 'stable'

# Request members
nestedMemberRequests = [
    '{id,contactDetails{id,name},org{id,name,short},email,membershipNumber}',
    '{id,email,paymentAmount,customFields{id,org{id,short},userObject,customField{name},value}}'
]

# Request contact-details
nestedContactDetailsRequests = [
    '{id,org,name,age,customFields{id,value}}',
    '{id,customFields{addressObject{customFields{addressObject{id}}}}}'
]

response = [None] * 2
# Get the entries as json from the server
for nestedMemberRequest, nestedContactDetailsRequest in zip(nestedMemberRequests, nestedContactDetailsRequests):

    response[0] = requests.get('https://easyverein.com/api/{version}/member?query={query}'.format(query=nestedMemberRequest, version=version), headers=header)
    response[1] = requests.get('https://easyverein.com/api/{version}/contact-details?query={query}'.format(query=nestedContactDetailsRequest, version=version), headers=header)
    
    for res in response:
        if res.status_code == 200 and len(res.content) < 500:
            print(res.content)

        else:
            print(res.status_code)
