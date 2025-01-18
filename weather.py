import requests

endpoint = "https://api.openweathermap.org/data/2.5/forecast/daily"
api_key = "ac55b629b9ca2af3c2165a3a6fb31cbc"

cordinates = {
    'lat':28.669155,
    'lon':77.453758,
    'appid': api_key,
}

response = requests.get(endpoint,params=cordinates)
print(response.json())