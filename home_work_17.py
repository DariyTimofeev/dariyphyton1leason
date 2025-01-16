import requests

response = requests.get("http://api.open-notify.org/astros.json")
data = response.json()
astronauts = data['people']
for astronaut in astronauts:
    print(astronaut['name'])