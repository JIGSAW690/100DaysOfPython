# Day49 - Gym Booking Automation Bot 🏋️🤖

## 📖 Overview
Day 49 of the 100 Days of Code challenge was about building a **real-world Selenium automation bot** that can log in, book classes, and verify reservations on a gym booking portal.

---

## 📂 Project Structure
Day49/

│── Gym_Booking_Automation_Bot/

│ ├── main.py # Automation bot script

---

## 🛠️ Features
- 🔑 Automated **Login** (with email & password)  
- 📅 Automatically detects **Tuesday & Thursday 6 PM** classes  
- 🖱 Handles different booking states:
  - `Book Class`
  - `Booked`
  - `Waitlisted`
  - `Join Waitlist`  
- 🔁 Implements a **retry wrapper** for robustness  
- ✅ Navigates to **My Bookings** and verifies reservations  

---

## 📜 Script Details
### main.py
- Creates a **custom Chrome profile** (`chrome_profile/`) to persist logins.  
- Uses `WebDriverWait` + `expected_conditions` to wait for elements dynamically.  
- Defines helper functions:
  - `retry(func)` → retries actions in case of `TimeoutException`
  - `login()` → automates login process
  - `book_class()` → books or waitlists a class
  - `get_my_bookings()` → navigates and verifies bookings
- Iterates over **class cards**, checking dates/times, and books if conditions match.  
- Prints verification results at the end.  

---

## 🚀 How to Run
1. Install requirements:
   ```bash
   pip install selenium
Download ChromeDriver matching your Chrome version.

Update your email & password in main.py:

ACCOUNT_EMAIL = "your_email"

ACCOUNT_PASSWORD = "your_password"

Run the script:
python main.py

## 🧠 Key Learnings
Using persistent Chrome profiles for smoother logins

Handling dynamic elements with WebDriverWait

Making automation resilient with retries

Real-world application of Selenium beyond practice scripts

## 🎯 Takeaway
This bot automates a real-life repetitive task — booking gym slots — showing how Selenium can save time and effort while ensuring accuracy.