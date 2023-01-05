import requests

BASE_URL = "https://feiertage-api.de/api/"
PARAMETER1 = "?jahr=2019"

response = requests.get(BASE_URL + PARAMETER1)

print(response.text)