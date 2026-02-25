# In newer versions (v1.5) of the api some endpoints like the /member/{userPk}/custom-fields can be used with a bulk-create and bulk-update
# For further information and to check which endpoints are enabled for the bulk actions see the documentation (https://easyverein.com/api/)

curl -X POST https://easyverein.com/api/v1.5/member/5485413/custom-fields/bulk-create \
-H 'Authorization: Bearer <YOUR-API-KEY>' -H 'Content-Type: application/json' \
-d'{"entries":[{"customField":53851,"value":"Linux btw"},{"customField":53852,"value":"sudo"}]}'
