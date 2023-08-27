import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "49b8139bcd54291e9f28126b7b0e14e4"

weather_params = {
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
print(response.status_code)
