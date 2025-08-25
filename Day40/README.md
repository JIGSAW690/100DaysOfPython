# ✈️ Flight Deals Finder

A Python project that tracks flight prices and notifies you when cheap flights are found.  
Built as part of my **#100DaysOfCode** journey (Day 40).  

---

## 🚀 Features
- Fetch destination cities + lowest price thresholds from **Google Sheet** (via Sheety API).
- Look up **IATA codes** automatically with the Amadeus "Airports & City Search" API.
- Search for flights (next 6 months) using the **Amadeus Flight Offers API**.
- Parse results to find the **cheapest flight**.
- Send notifications:
  - 📱 **SMS/WhatsApp** via Twilio
  - 📧 **Email alerts** via SMTP
- Runs automatically on **PythonAnywhere**.

---

## 🛠️ Tech Stack
- **Python**
- **APIs**: Amadeus, Sheety, Twilio
- **Libraries**: `requests`, `smtplib`, `twilio`

---

## 📂 Project Structure
.
├── main.py # Entry point

├── data_manager.py # Handles Google Sheet (Sheety API)

├── flight_search.py # Amadeus API calls (IATA lookup + flight offers)

├── flight_data.py # FlightData class + cheapest flight parser

├── notification_manager.py # SMS, WhatsApp & Email alerts

---

## 🔑 Setup Instructions

1. **Clone repo & install dependencies**
   ```bash
   git clone <repo-url>
   cd flight-deals-finder
   pip install -r requirements.txt
  ``` 

Set environment variables

Create a .env file or set in your shell:


ENDPOINT= your Sheety prices endpoint

SHEETY_USERS_ENDPOINT= your Sheety users endpoint

TOKEN= your Sheety bearer token 

AMADEUS_API_KEY= your amadeus api key 

AMADEUS_SECRET= your amadeus secret

TWILIO_SID= your twilio sid

TWILIO_AUTH_TOKEN= your twilio token

MESSAGING_SERVICE_SID= your twilio messaging service sid

TWILIO_VERIFIED_NUMBER= your verified phone number

EMAIL_PROVIDER_SMTP_ADDRESS= smtp.gmail.com or similar

MY_EMAIL= your email

MY_EMAIL_PASSWORD= your email app password

```

**Run script** 

python main.py

**⚡ Automation**

I deployed this project on PythonAnywhere to run daily.
This way, I get notified about flight deals automatically without needing to keep my laptop running.

**📌 Example Alert**

Low price alert! Only £199 to fly from CCU to CDG,
departing on 2025-09-12 and returning on 2025-09-28.

**🏆 Learning Outcomes**

Working with multiple APIs in one project

Automating tasks with schedulers (PythonAnywhere)

Handling rate limits & authentication (OAuth2)

Sending SMS, WhatsApp, and emails programmatically

## 💡 Inspired by Day 40 of 100 Days of Code (Python Bootcamp).






