# JokeAPI is a REST API that serves uniformly and well formatted jokes.

import requests
from time import sleep

request=requests.get('https://v2.jokeapi.dev/joke/Any?',{'lang':'en'})
info=request.json()


if info['type']=='single':
    print(info['joke'])
    
elif info['type']=="twopart":
    print(info['setup'])
    sleep(3)
    print(info['delivery'])
    