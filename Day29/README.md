# Day 29 – Password Manager App 🔐

## 📌 Overview
A simple yet effective **Password Manager** built with **Python Tkinter** that allows users to store website credentials locally in a text file.

---

## 🖼 Features
- **Input Fields:** Website URL, Email, Password
- **Password Generator** to create strong passwords instantly
- **Add Button** saves credentials in the format:
      Website | Email | Password
- **Validation Checks:**
  - All fields must be filled
  - Email must end with `.com`
- **Error Dialogs** for incorrect or incomplete inputs

---

## 📂 Project Structure
Day29/

└── password-manager-start/

├── main.py       # Main application code

├── logo.png      # App logo displayed in UI

├── data.txt      # Generated after first save

└── README.md     # Project documentation

---

## 🚀 How to Run
1. **Clone the repository**
```bash
git clone https://github.com/<your-username>/Day29.git
cd Day29/password-manager-start
```
2.	**Run the application**

python main.py

3.	**Using the app**

o	Enter Website URL, Email, and Password.

o	Use the Generate Password button for a random secure password.

o	Click Add to save credentials in data.txt.

## 🛠 Skills Learned
•	Tkinter GUI development

•	Input validation

•	File handling in Python

•	Dialog boxes for error handling

•	Simple password generation logic

