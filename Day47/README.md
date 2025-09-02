# 🛒 Automated Amazon Price Tracker App  

A Python automation project that tracks the price of a product on Amazon and sends you an **email alert** when the price falls below your desired threshold.  
Deployed on **PythonAnywhere** for daily scheduled checks.  

---

## 🚀 Features  
- Scrapes live product data from Amazon  
- Extracts **product title** and **current price**  
- Compares price against a predefined **BUY_PRICE**  
- Sends an **email notification** when price drops  
- Runs daily on **PythonAnywhere**  

---

## 🛠️ Tech Stack  
- **Python**  
- [BeautifulSoup (bs4)](https://pypi.org/project/beautifulsoup4/) → Parse product HTML  
- [Requests](https://pypi.org/project/requests/) → Fetch Amazon product page  
- [smtplib](https://docs.python.org/3/library/smtplib.html) → Send email notifications  
- **os** → Manage environment variables securely  

---

## 📂 Project Structure  

Day47/

│── Automated Amazon Price Tracker App/

│ │── main.py # Main script

│ │── .idea/ # IDE settings (optional)


---

## ⚙️ Setup Instructions  

1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/Amazon-Price-Tracker.git
   cd Amazon-Price-Tracker
   ```
## Install dependencies:

pip install requests beautifulsoup4

Set environment variables (either in .env, system environment, or PythonAnywhere):

export ENDPOINT="https://www.amazon.com/dp/PRODUCT_ID"

export SMTP_ADDRESS="smtp.gmail.com"

export EMAIL="your_email@gmail.com"

export PASS="your_email_password_or_app_password"

Update BUY_PRICE in main.py to your desired threshold.

Run the script manually:

python main.py

(Optional) Automate with PythonAnywhere

Upload project files

Add a daily scheduled task to run python3 main.py

Receive email notifications automatically 📩


## 📌 Notes
Works best with Amazon’s desktop site HTML (may require updating user-agent headers).

Email sending requires enabling App Passwords if using Gmail.

Use responsibly—don’t overload Amazon with requests.

## 📜 License
This project is for learning and personal use only. Not affiliated with Amazon.