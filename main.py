from requests import *
from datetime import datetime

API_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "gokulbakkiyarasu"
TOKEN = "exif33waihcaweihwiheclIE3HF1YFEIHFWE5IFH6wifi"
pixela_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# create an account using post method
response = post(url=API_ENDPOINT, json= pixela_parameters)
print(response.text)

graph_endpoint = f"{API_ENDPOINT}/{USERNAME}/graphs"
graph_parameters = {
    "id": "graph2",
    "name": "Cycling graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}
header = {
    "X-USER-TOKEN": TOKEN
}
# creating pixel graph
response = post(url=graph_endpoint, json=graph_parameters, headers=header)
print(response.text)

today = datetime.now()
pixel_endpoint = f"{API_ENDPOINT}/{USERNAME}/graphs/graph2"
pixel_parameters = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "30",
}

# posting response to a pixela graph
response = post(url=pixel_endpoint, json=pixel_parameters, headers=header)
print(response.text)

update_pixel_endpoint = f"{API_ENDPOINT}/{USERNAME}/graphs/graph2/{pixel_parameters['date']}"
update_data = {
    "quantity": "80"
}
# updating existing data
response = put(url=update_pixel_endpoint, json=update_data, headers=header)
print(response.text)

# deleting existing data
response = delete(url=update_pixel_endpoint, headers=header)
print(response.text)