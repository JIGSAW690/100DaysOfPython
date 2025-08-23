# 🎉 Day 32 Projects - Birthday Wisher & Monday Motivation Generator

Two automation-focused Python projects built as part of **Day 32 of 100 Days of Python**. 
Both projects leverage email automation with simple yet effective logic.

---

## 🚀 Projects

### 1️⃣ Monday Motivation Generator
- Sends an **email every Monday morning** with a random motivational quote.
- Reads quotes from `quotes.txt`.
- Uses:
- `datetime` → to check if today is Monday
- `random` → to select a quote
- `smtplib` → to send email via SMTP server

---

### 2️⃣ Birthday Wisher
- Sends **personalized birthday wishes** to people listed in `birthdays.csv`.
- Picks a **random letter template** from the `letter_templates/` directory.
- Replaces `[NAME]` placeholder in the letter with the recipient’s name.
- Sends the birthday email using `smtplib`.
- Automated scheduling done with **PythonAnywhere**.
- Uses:
- `datetime` → to check if today matches a birthday
- `pandas` → to read & manage `birthdays.csv`
- `random` → to pick a random letter template
- `smtplib` → for email sending

---

## 🗂️ Project Structure

Birthday Wisher (Day 32) start/

├── letter_templates/

│   ├── letter_1.txt

│   ├── letter_2.txt

│   └── letter_3.txt
│
├── birthdays.csv              # Birthday dataset

├── main.py                    # Birthday Wisher script

├── monday_motivation.py       # Monday Motivation script

└── quotes.txt                 # Motivational quotes

---

## ⚙️ Setup & Run

1. Clone or download this project.
2. Update your email & password (or App Password) in the scripts.
3. Run the desired script:
```bash
python monday_motivation.py
python main.py

4.	For automation:
o	Use Task Scheduler / cron jobs locally
o	Or deploy to PythonAnywhere for cloud scheduling
```
________________________________________
**🎯 Learning Outcomes**

•	Working with dates & times in Python

•	Automating emails with smtplib

•	Using randomization for variety

•	Handling CSV files with pandas

•	Deploying & scheduling scripts on the cloud
________________________________________
**🌟 Future Improvements**

•	Add HTML email templates for rich formatting

•	Track email delivery status

•	Integrate with external APIs for quotes/birthdays
