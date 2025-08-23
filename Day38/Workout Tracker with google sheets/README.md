# Day 38 – Workout & Calorie Tracker App 🏋️‍♂️🔥

## 📌 Project Overview
This Python project allows you to log your daily exercises and automatically track them in a **Google Sheet**.  
It integrates with the **Nutritionix API** to fetch calories burned and duration of workouts, and then updates the sheet via the **Sheety API**.

---

## ⚙️ Features
- Input your workout (e.g., "Ran 3 km and cycled for 20 minutes")
- Fetch details (exercise type, duration, calories burned) from Nutritionix
- Store results in Google Sheets (date, time, exercise, duration, calories)
- Uses **Bearer Token Authentication** for secure sheet updates
- Environment variables are used for sensitive information (App ID, API Key, Token, Endpoints)

---

## 🛠️ Tech Stack
- **Python**
- **Nutritionix API** (for exercise details)
- **Sheety API** (to store in Google Sheets)
- **Environment Variables** (via `os` module)
- **Datetime module** (for date and time formatting)

---

## 📂 Directory Structure
Day38/

├── README.md

└── workout_tracker.py

---

## 🚀 How to Run
1. Clone the repo and navigate to `Day38/`.
2. Install dependencies (requests):
   ```bash
   pip install requests
Set up your environment variables:


export APP_ID=your_app_id

export API_KEY=your_api_key

export TOKEN=your_sheety_token

export SHEET_ENDPOINT=your_sheety_endpoint

**Run the script:**

python main.py

Enter your exercises when prompted. The results will automatically appear in your Google Sheet!

## 🔒 Security Note

All sensitive values (App ID, API Key, Token, Endpoint) are stored in environment variables instead of hardcoding them in the codebase. This ensures better security and follows DevOps best practices.

## 📊 Example Output (Google Sheet Entry)

Date	Time	Exercise	Duration	Calories

23/08/2025	11:30:00	Running	30 min	250 kcal

23/08/2025	11:30:00	Cycling	20 min	180 kcal

