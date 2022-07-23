# code by aadhaar koul
# mail - aadhaarkoul2002@gmail.com
# this is a simple python code that make a simple api request
# to fetch the kanye west quotes from the internet ad prints them on the screen

import requests

response = requests.get(url='http://api.kanye.rest')
response.raise_for_status()

data = response.json()

quote = data["quote"]

print(quote)

# run and see the magic