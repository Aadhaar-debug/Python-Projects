# finding out where the iss is currentlky hovering in the sky over the earth
# APi or application program interface
# an api is a main line of connection between your program and the external system

import requests
response = requests.get(url='http://api.open-notify.org/iss-now.json')
response.raise_for_status()

data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)

print(iss_position)


# is the response code is equal to
#  1XX - Hold on , 2XX - Here you go , 3XX - Go away , 4XX - Yoy screwed up , 5XX - I screwed up

