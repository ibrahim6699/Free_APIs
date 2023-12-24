# Quotable is a free, open source quotations API.
# It was originally built as part of a FreeCodeCamp project

import requests

request=requests.get('https://api.quotable.io/random')
info=request.json()

print(info['content'])
print(info['author'])