url='https://easyverein.com/api/stable/member/{pk}/'

curl $url -X PATCH -H 'Authorization: Bearer <YOUR-API-KEY>' -F '_profilePicture=@/path/to/your/file.png'
