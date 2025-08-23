import requests
import os
import datetime as dt

today = dt.datetime.now()
formatted_date = today.strftime("%d/%m%Y")
now_time = today.strftime("%X")

APP_ID = os.environ.get("APP_ID")  #Stored in environment variables
API_KEY = os.environ.get("API_KEY")  #Stored in environment variables
TOKEN = os.environ.get("TOKEN")  #Stored in environment variables
sheet_endpoint = os.environ.get("SHEET_ENDPOINT")  #Stored in environment variables

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"


exercise_params = {
    "query": input("What exercises you did today?\t")
}

sheet_params = {}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

response = requests.post(url=nutritionix_endpoint, json=exercise_params, headers=headers)
result = response.json()

for exercise in result["exercises"]:
    sheet_params = {
        "sheet1": {
            "date": formatted_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

#Bearer Token Authentication
bearer_headers = {
    "Authorization": f"Bearer {TOKEN}"
}

sheet_response = requests.post(url=sheet_endpoint, json=sheet_params, headers=bearer_headers)
print(sheet_response.text)

