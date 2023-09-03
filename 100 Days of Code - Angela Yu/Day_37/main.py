import requests

from datetime import datetime

USERNAME = "visesh"
Token = "lkhsdfksdflkjasdfasfhwuer"
Graph_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": Token,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": Graph_ID,
    "name": "Python Course",
    "unit": "videos",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": Token
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{Graph_ID}"

today = datetime(year=2023, month=9, day=2)

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10",
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)