import requests
import datetime as dt
import os

#CREATING DATE AS MENTIONED IN POST-PIXEL DOCS
today = dt.datetime.now()
formatted_date = today.strftime('%Y%m%d')

username = os.environ.get('USERNAME')
token = os.environ.get('TOKEN')
graph_id = os.environ.get('GRAPH_ID')

#Endpoints
user_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{user_endpoint}/{username}/graphs"
pixel_endpoint = f"{graph_endpoint}/{graph_id}"
pixel_update_endpoint = f"{pixel_endpoint}/{formatted_date}"

#Parameter to create a new PIXELA user
user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#Parameter for setting up the Graph
graph_params = {
    "id": graph_id,
    "name": "CyclingTracker",
    "unit": "kilometer",
    "type": "float",
    "color": "momiji"
}

#HEADER for securely connecting to endpoints
header = {
    "X-USER-TOKEN": token
}

#Parameter for pixel POST
pixel_params = {
    "date": formatted_date,
    "quantity": input('How many Kms have you cycled today?\t')
}

#Parameter for pixel UPDATE/PUT
pixel_update_params = {
    "quantity": "32.2"
}

"""
The ENDPOINT for DELETE is same as the endpoint for PUT, 
only difference being The DELETE endpoint don't accept any parameters
"""

response = requests.put(url=pixel_update_endpoint, json=pixel_update_params, headers=header)
print(response.text)