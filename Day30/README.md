# Day 30 – Exception Handling & Project Upgrades

## 📅 Overview
On Day 30 of my **100 Days of Python** journey, I focused on **exception handling** — making my code more **reliable** and **user-friendly** by gracefully dealing with errors. 
I also enhanced two projects to incorporate better error handling and improved data storage.

---

## 🛠 Concepts Learned
- Using `try`, `except`, `else`, `finally` blocks
- Raising custom exceptions with `raise`
- Handling common errors:
  - `FileNotFoundError`
  - `TypeError`
  - `KeyError`
  - `IndexError` (IndexOutOfBounds)
- Validating user input until correct
- Reading & writing JSON files with Python’s `json` module

---

## 📂 Projects

### 1️⃣ NATO Phonetic Alphabet (Improved)
**Description:**
- User enters a word, and the program returns a list of words from the NATO alphabet that start with each letter of the input.
- If the user enters numbers or invalid input, the program **keeps asking** until a valid word is entered.

**Features:**
- Persistent error handling
- Prevents crashes on invalid input
- Demonstrates input validation with exception handling

**Example:**

Enter a word: 123 ❌

Please enter a valid word

Enter a word: Chat

[‘Charlie’, ‘Hotel’, ‘Alpha’, ‘Tango’]

---

### 2️⃣ Password Manager App (Enhanced)
**Description:**
- Built using Tkinter for the GUI.
- Allows saving, generating, and searching for passwords.
- Stores credentials in a **JSON file** instead of a `.txt` file for better structure.

**Features:**
- **Add Credentials:** Website, Email, Password (generated or manually entered)
- **Search:** Check if credentials for a website already exist
- **Data Storage:** Stores as JSON:
```json
{
"example.com": {
"email": "user@example.com",
"password": "P@ssw0rd123"
}
}

•	Validation:
o	No empty fields allowed
o	Email must end with .com
•	Error Handling:
o	Uses try-except to handle FileNotFoundError when searching in an empty database
o	Displays error dialogs for invalid inputs
________________________________________
📁 Directory Structure
Day30/
│
├── nato_project/
│ ├── main.py
│
├── password_manager/
│ ├── main.py
│ ├── logo.png
│ ├── data.json (auto-created)


🚀 How to Run
1.	Clone the repository or navigate to the respective project folder.
2.	Install dependencies (only Tkinter needed, which comes pre-installed in Python for most OS).
3.	Run the project:
python main.py

🖥 Preview

Password Manager App GUI Example:
•	Fields for Website, Email, and Password
•	Buttons: “Generate Password”, “Add”, “Search”
•	Clean, simple Tkinter interface
________________________________________
```

**📌 Learnings**

This day really helped me understand how important exception handling is in making a project user-friendly and bug-free.

Also learned how JSON can make data more structured and easier to work with compared to plain text.
