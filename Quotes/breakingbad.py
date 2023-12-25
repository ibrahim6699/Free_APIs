# A free API to retrieve some quotes of Breaking Bad, bitch!

import requests


response = requests.get("https://api.breakingbadquotes.xyz/v1/quotes")

# Check if the request was successful (status code 200)
if response.ok:
    try:
        json_data = response.json()
        print(json_data[0]['quote'])
        print(json_data[0]['author'])

    except requests.exceptions.JSONDecodeError as e:
        print("Error decoding JSON:", e)
else:
    print("Request failed with status code:", response.status_code)
