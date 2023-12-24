# The Geek Jokes RESTful API lets you fetch a random geeky/programming
# related joke for use in all sorts of applications.

import requests

request=requests.get('https://geek-jokes.sameerkumar.website/api?format=json')
info=request.json()

print(info['joke'])