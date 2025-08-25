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
        #self._user = os.environ["SHEETY_USERNAME"]
        #self._password = os.environ["SHEETY_PASSWORD"]
        # Save your Sheety endpoints an environment variables
        self.prices_endpoint = os.environ["ENDPOINT"]
        self.users_endpoint = os.environ["SHEETY_USERS_ENDPOINT"]
        # Destination and Customer fields data start out empty
        self.destination_data = {}
        self.customer_data = {}

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

    def get_customer_emails(self):
        response = requests.get(url=self.users_endpoint)
        data = response.json()
        # See how Sheet data is formatted so that you use the correct column name!
        # pprint(data)
        # Name of spreadsheet 'tab' with the customer emails should be "users".
        self.customer_data = data["users"]
        return self.customer_data
