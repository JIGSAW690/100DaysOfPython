import requests
from twilio.rest import Client
import os
import datetime as dt

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

#Sensitive Values
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
STOCK_API_KEY =  os.environ.get("STOCK_API_KEY") # "IRAHIDJHQ7UJ36F5"
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
MESSAGING_SERVICE_SID = os.environ.get("MESSAGING_SERVICE_SID")

stock_params = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK,
    "interval": "60min",
    "apikey": STOCK_API_KEY,
}

news_params = {
    "q": COMPANY_NAME,
    "from": yesterday_str,
    "sortBy": "popularity",
    "apiKey": NEWS_API_KEY,
}

news_data = {}
is_price_changed = False


today = dt.datetime.now()
yesterday = today - dt.timedelta(days=1)
day_before_yesterday = today - dt.timedelta(days=2)
# Format dates as strings for API
yesterday_str = yesterday.strftime("%Y-%m-%d")
day_before_yesterday_str = day_before_yesterday.strftime("%Y-%m-%d")

#Get the first 3 news pieces for the COMPANY_NAME.
def get_news():
    global news_data
    news_response = requests.get(url="http://newsapi.org/v2/everything", params=news_params, verify=False)
    news_data = news_response.json()


# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then send message.
response = requests.get(url="http://www.alphavantage.co/query", params=stock_params, verify=False)
#print(response.json())
yesterday_price = float(response.json()["Time Series (60min)"][f"{yesterday_str} 19:00:00"]["4. close"])
day_before_yesterday_price = float(response.json()["Time Series (60min)"][f"{day_before_yesterday_str} 19:00:00"]["4. close"])

price_change_percentage = abs((yesterday_price - day_before_yesterday_price) / day_before_yesterday_price * 100)
if price_change_percentage >= 5:
    get_news()
    is_price_changed = True

def send_message():
    client = Client(account_sid, auth_token)
    for i in range(3):
        if yesterday_price > day_before_yesterday_price:
            message = client.messages.create(
                messaging_service_sid=MESSAGING_SERVICE_SID,
                body=f"{STOCK}: 🔺 {price_change_percentage}%\n"
                     f"Headline: {news_data['articles'][i]['title']}\n"
                     f"Brief: {news_data['articles'][i]['description']}\n",
                to='+917063300272'
            )
            print(message.status)
        else:
            message = client.messages.create(
                messaging_service_sid=MESSAGING_SERVICE_SID,
                body=f"{STOCK}: 🔻{price_change_percentage}%\n"
                     f"Headline: {news_data['articles'][i]['title']}\n"
                     f"Brief: {news_data['articles'][i]['description']}\n",
                to='+917063300272'
            )
            print(message.status)


# Send a seperate message with the percentage change and each article's title and description to your phone number.
if is_price_changed:
    send_message()


