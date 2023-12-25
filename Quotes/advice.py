# The Advice Slip JSON API is provided for free. 😎 
# It currently gives out over 10 million pieces of advice every year.

import requests

response = requests.get("https://api.adviceslip.com/advice")

# Check if the request was successful (status code 200)
if response.ok:
    try:
        json_data = response.json()
        print(json_data['slip']['advice'])
    except requests.exceptions.JSONDecodeError as e:
        print("Error decoding JSON:", e)
else:
    print("Request failed with status code:", response.status_code)
