# icanhazdadjoke.com can be used as an API for fetching a random joke,
# a specific joke, or searching for jokes in a variety of formats

import requests

request=requests.get('https://icanhazdadjoke.com/slack')

info=request.json()

print(info['attachments'][0]['text'])