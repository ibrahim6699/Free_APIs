# chucknorris.io is a free JSON API 
# for hand curated Chuck Norris facts

import requests


request=requests.get('https://api.chucknorris.io/jokes/random')
info=request.json()

print(info['value'])