import requests

AMOUNT = 10
TYPE = "boolean"

parameter = {
    "amount": AMOUNT,
    "type": TYPE,
}

response = requests.get(url="https://opentdb.com/api.php", params=parameter, verify=False)
response.raise_for_status()
data = response.json()

question_data = data["results"]
#print(question_data)