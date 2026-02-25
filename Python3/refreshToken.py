# Since v2.0, the API enforces the use of a new kind of token that must get refreshed after a certain time.
# This token can be refreshed using the `refresh-token` endpoint from v2.0 or newer.
# Legacy tokens can be replaced by a new one using the `refresh-token` endpoint.
# The new tokens can also be used for versions below v2.0

import requests

# Send a request that is answered by the API with the header attribute `tokenRefreshNeeded` set to True
header={'Authorization': 'Bearer <YOUR-API-KEY>'}
response = requests.get('https://easyverein.com/api/stable/member/', headers=header)
# NOTE: currently the v2.0 is only available using the hexa.easyverein.com domain. However, this will be changed  back to easyverein.com in the future

tokenRefreshNeeded = response.headers.get('tokenRefreshNeeded')

if tokenRefreshNeeded:
    # NOTE: `refresh-token` is only available in v2.0 or newer
    response = requests.get('https://easyverein.com/api/latest/refresh-token/', headers=header)
    newToken = response.json().get('Bearer')
