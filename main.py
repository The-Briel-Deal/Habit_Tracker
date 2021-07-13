import requests
import os
import datetime
# ----- SETTING VARIABLES ----- #
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = 'therealbriel'
TOKEN = os.environ.get('token')
user_params = {'token': TOKEN,
               'username': USERNAME,
               'agreeTermsOfService': 'yes',
               'notMinor': 'yes'
               }

# ----- POSTING TO PIXELA ----- #
# response = requests.post(url=pixela_endpoint, json=user_params)therealbriel
# print(response.text)

date = datetime.datetime.now().strftime(f'%Y%m%d')
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{date}"

print(date)

graph_config = {
    'id': 'graph1',
    'name': 'League Graph',
    'unit': 'Wins',
    'type': 'float',
    'color': 'momiji',
}
push_pixel = {
    'date': date,
    'quantity': '1'
}

put_pixel = {
    'quantity': '3'
}

headers = {
    'X-USER-TOKEN': TOKEN

}
response = requests.put(url=graph_endpoint, json=put_pixel, headers=headers)
print(response.text)
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
