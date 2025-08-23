# ☔ Rain Alert App (Day 35 Project)

A Python app that checks the daily weather forecast and sends an SMS reminder at **6 AM IST** to let me know if I need to carry an umbrella 🌂. 

---

## 🚀 Features
- Fetches **weather forecast** from [OpenWeatherMap API](https://openweathermap.org/forecast5)
- Runs **daily at 6 AM IST**
- If rain is expected → Sends an **SMS alert** via Twilio
- API Keys and Auth Tokens are stored securely as **environment variables**

---

## 🗂️ Project Structure

Day35/

├── README.md

└── Rain_alert_app/
|
└── main.py

---

## ⚙️ How It Works
1. **Weather Data Fetching**
- Uses the `requests` module to get forecast data from:
```
https://api.openweathermap.org/data/2.5/forecast
```
- Query parameters:
- `lat` → Latitude of location
- `lon` → Longitude of location
- `appid` → API key (stored in env vars)
- `cnt` → Number of forecast entries you want to check for the whole day

2. **Rain Check**
- Parses the forecast JSON response
- Checks if `"rain"` exists in the weather data by comparing the weather codes

3. **Send SMS**
- If rain is expected → Sends **"Carry an Umbrella ☔"** SMS
- If not → Sends **"No Umbrella Needed ✅"** SMS
- Uses the `twilio.Client` class to send SMS

---

## 🛠️ Tech Stack
- **Python Modules**:
- `os` → Manage environment variables
- `requests` → API call
- `twilio` → Send SMS
- **APIs**:
- [OpenWeatherMap Forecast API](https://openweathermap.org/forecast5)
- [Twilio Messaging API](https://www.twilio.com/)

---

## 🔒 Security (Environment Variables)
This app uses **environment variables** to store sensitive credentials like:
- `OWM_API_KEY` → OpenWeatherMap API key
- `TWILIO_AUTH_TOKEN`


This prevents secrets from being hardcoded in the source code, keeping the app secure and production-ready.

---

## 🕒 Scheduling
Currently, the app is configured to run at **6 AM IST** daily. 
You can schedule it using:
- **cron jobs** (Linux/macOS)
- **Task Scheduler** (Windows)
- Container-based schedulers in DevOps pipelines
- Or using PythonAnywhere to schedule the task of running the app daily on a mentioned time

---

## 🎯 Learning Outcomes
- Fetching and parsing weather data from APIs
- Automating daily tasks with Python
- Sending SMS alerts via Twilio
- Using **environment variables** for secret management
- Scheduling tasks to run at specific times
