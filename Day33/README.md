# 🌍 Day 33 Projects - Working with APIs

Day 33 was all about learning how to work with **APIs in Python** using the `requests` module. 
I built **two projects** to put this into practice.

---

## 🚀 Projects

### 1️⃣ Kanye Quotes App
- A simple **Tkinter-based app** that fetches and displays random Kanye West quotes.
- API Used: [Kanye Rest API](https://api.kanye.rest)
- Modules:
- `requests` → fetch random quotes
- `tkinter` → build UI and display quotes on a canvas
- Functionality:
- A Kanye button is placed on the UI
- Clicking it triggers an API call and updates the canvas with a new quote

---

### 2️⃣ ISS Overhead Notifier
- Sends an **email alert** when the **International Space Station** is above the user’s location at night.
- APIs Used:
- `http://api.open-notify.org/iss-now.json` → Current ISS position
- `https://api.sunrise-sunset.org/json` → Sunrise and sunset times for today
- Modules:
- `requests` → fetch ISS position and sunrise/sunset data
- `datetime` → check current time
- `smtplib` → send email
- `time` → keep checking periodically
- Logic:
1. Check if ISS is within **±5°** of given latitude & longitude
2. Check if current time is **between sunset and sunrise**
3. If both conditions are met → send email notification to look up at the sky 🌌

---

## 🗂️ Project Structure

Day33/

├── issoverhead-start/

│   ├── config.py       # Email credentials / config

│   └── main.py         # ISS Overhead Notifier

├── kanye-quotes-start/

│   ├── background.png  # Tkinter canvas background

│   ├── kanye.png       # Kanye button image

│   └── main.py         # Kanye Quotes App

└── README.md

---

## ⚙️ Setup & Run

### Kanye Quotes App
1. Run:
```bash
python kanye-quotes-start/main.py
```

2.	Click on Kanye button → new random quote appears

### ISS Overhead Notifier
1.	Add your latitude, longitude, and email details in config.py
2.	Run:
python issoverhead-start/main.py

3.	The script will check ISS location & send an email if conditions match
________________________________________

**🎯 Learning Outcomes**

•	Using the requests library to interact with APIs

•	Integrating API responses with UI and automation

•	Email automation with smtplib

•	Real-world applications of Python APIs
________________________________________

**🌟 Future Improvements**

•	Add GUI alert for ISS overhead (in addition to email)

•	Improve exception handling for API downtime

•	Support multiple recipients for birthday/email alerts
