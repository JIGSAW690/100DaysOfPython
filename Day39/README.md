# Day 39 – Flight Deals Finder App ✈️

## 📌 Project Overview
This Python app checks for cheap flights from **London (LON)** to various destinations and notifies the user if the price drops below a pre-set threshold.  
It integrates **Amadeus API** for flight data, **Sheety API** for storing city and price data in Google Sheets, and **Twilio API** for sending SMS notifications.

---

## ⚙️ Features
- Fetches city and price data from Google Sheets (via Sheety API)
- Retrieves IATA airport codes for each city using Amadeus Location API
- Searches for flights within the next 6 months
- Finds the **cheapest flight option** from the available results
- Sends **SMS alerts** for low-price deals via Twilio API
- Secure storage of sensitive data in **environment variables**

---

## 🛠️ Tech Stack
- **Python**
- **Amadeus API** (flight offers + city codes)
- **Sheety API** (Google Sheets integration)
- **Twilio API** (SMS notifications)
- **Environment Variables** (via `os` module)
- **Datetime** (for managing flight dates)

---

## 📂 Directory Structure
Day39/

├── data_manager.py # Handles Google Sheets (Sheety API)

├── flight_data.py # Defines FlightData class and cheapest flight logic

├── flight_search.py # Handles Amadeus API (IATA codes + flight offers)

├── main.py # Main driver script

└── notification_manager.py # Handles Twilio SMS notifications

---

## 🚀 How to Run
1. Clone the repo and navigate to `Day39/`.
2. Install dependencies:
   ```bash
   pip install requests twilio
Set up your environment variables:

export ENDPOINT=your_sheety_endpoint
export TOKEN=your_sheety_token
export AMADEUS_API_KEY=your_amadeus_api_key
export AMADEUS_SECRET=your_amadeus_secret
export TWILIO_SID=your_twilio_sid
export TWILIO_AUTH_TOKEN=your_twilio_auth_token
export TWILIO_VERIFIED_NUMBER=your_verified_number
Run the script:

python main.py

If a cheap flight is found, you’ll receive an SMS notification instantly 📲.

## 📊 Example Notification

Low price alert! Only £95 to fly from LHR to CDG,
on 2025-09-15 until 2025-09-22.
🔒 Security Note
All API keys, tokens, and secrets are stored in environment variables. Never hardcode sensitive values into the source code. This follows best practices for DevOps and production-ready apps.