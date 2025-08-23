# 📈 Stock Notifier App 

This project is part of **Day 36 of 100 Days of Python**. 
The Stock Notifier App alerts you via **SMS** when a company’s stock price fluctuates by more than **5%** compared to the previous day. 

---

## 🚀 Features 
- Fetches **stock data** from [Alpha Vantage API](https://www.alphavantage.co/query) 
- Calculates **daily percentage change** in closing price 
- If change ≥ 5%: 
- Fetches **top 3 news articles** from [News API](https://newsapi.org/v2/everything) 
- Sends **SMS alerts** with headlines using [Twilio](https://www.twilio.com/) 

---

## 🛠️ Tech Stack 
- **Python 3** 
- `requests` → Fetch stock + news data 
- `twilio.rest` → Send SMS notifications 
- `os` → Manage sensitive values via environment variables 

---

## 📂 Project Structure 
Day36/

│── stock-news-extrahard-start/

│   │── project_config/          # (Config, env setup if any)

│   │── main.py                  # Main script with stock + news logic

│── README.md                    # Project documentation

---

## 🔑 Environment Variables 

Set the following variables in your environment before running: 

```bash
export ALPHA_VANTAGE_API_KEY="your_alpha_vantage_api_key"
export NEWS_API_KEY="your_newsapi_key"
export TWILIO_SID="your_twilio_account_sid"
export TWILIO_AUTH_TOKEN="your_twilio_auth_token"
export TWILIO_MESSAGE_SID="your_twilio_MESSAGE_SID"
```


▶️ How to Run
1.	Clone the repo and navigate to Day36 folder
2.	Install dependencies (if not already available):
pip install requests twilio

3.	Set up your environment variables (see above)
4.	Run the app:
python main.py

🔒 Security Note

All API keys and credentials are stored in environment variables, not in code. This ensures sensitive information remains secure and is a best practice in production-grade applications.
