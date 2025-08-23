import os
import requests
from twilio.rest import Client

#These values can be retrieved only after logging into the official site. These credentials will not work for persons other than me
account_sid = 'AC7c60f6f4f7e8b5edb8fa0232083dbe86'
auth_token = os.environ.get('AUTH_TOKEN')

weather_parameters = {
    "lat": 26.850889,
    "lon": 80.489929,
    "appid": os.environ.get('OWM_API_KEY'),
    "cnt": 4,
}

response = requests.get(url="http://api.openweathermap.org/data/2.5/forecast", params=weather_parameters)
response.raise_for_status()
will_rain = False
for i in range(0, 4):
    weather_data  = response.json()["list"][i]['weather']
    if weather_data[0]["id"] < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        messaging_service_sid='MG1f7729ea3fb62485ef6bde83a119c289',
        body="It'll rain today, carry an ☂️",
        to='+917063300272'
    )
    print(message.status)
