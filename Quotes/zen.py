# easy API to use

import requests

request =requests.get('https://zenquotes.io/api/random/')
info=request.json()

print(info[0]['q'])
print(info[0]['a'])