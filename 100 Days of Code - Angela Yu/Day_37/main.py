import requests

USERNAME = "visesh"
Token = "lkhsdfksdflkjasdfasfhwuer"

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
    "id": "graph1",
    "name": "Python Course",
    "unit": "videos",
    "type": "int",
    "color": "kuro"
}

headers = {
    "X-USER-TOKEN": Token
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

