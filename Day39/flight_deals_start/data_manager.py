import os
import requests
import pprint

sheety_prices_endpoint = os.environ.get('ENDPOINT')
TOKEN = os.environ.get('TOKEN')

#Bearer Token Authentication
bearer_headers = {
    "Authorization": f"Bearer {TOKEN}"
}

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        sheet_response = requests.get(url=sheety_prices_endpoint, headers=bearer_headers)
        data = sheet_response.json()
        self.destination_data = data["prices"]
        pprint.pprint(data)
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCodes": city['iataCodes']
                }
            }
            response = requests.put(
                url=f"{sheety_prices_endpoint}/{city['id']}",
                json=new_data,
                headers=bearer_headers
            )
            print(response.text)
