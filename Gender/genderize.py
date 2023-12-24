# simple API usage to get the gender by first name

import requests


name=input('What is the name?\n')
params={'name':name}

request=requests.get("https://api.genderize.io?",params=params)
info=request.json()

print(f'name : {name}')
print(f'gender : {info['gender']}')
print(f'probability : {info['probability']}')