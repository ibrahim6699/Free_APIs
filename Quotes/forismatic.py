# API method calls are implemented in the form of HTTP requests to the URL
# http://api.forismatic.com/api/1.0/

import requests

params={'method':'getQuote','format':'json','lang':'en'}
response = requests.post("http://api.forismatic.com/api/1.0/",params=params)

# Check if the request was successful (status code 200)
if response.ok:
    try:
        json_data = response.json()
        print(json_data['quoteText'])
        print(json_data['quoteAuthor'])
    except requests.exceptions.JSONDecodeError as e:
        print("Error decoding JSON:", e)
else:
    print("Request failed with status code:", response.status_code)
