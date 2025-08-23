# Day 26 – List & Dictionary Comprehension + NATO Alphabet Project

## 📌 Overview
Today's focus was on **Python Comprehensions** – a cleaner and faster way to create lists and dictionaries in just one line of code.  
Also, I learned how to use **dictionary comprehension with Pandas** to generate mappings from CSV data.

---

## 📝 Topics Covered
- **List Comprehension**
  ```python
  numbers = [n * 2 for n in range(1, 6)]
  # Output: [2, 4, 6, 8, 10]
• **Dictionary Comprehension**

squared_nums = {n: n**2 for n in range(1, 6)}
 Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

•	**From Pandas DataFrame to Dictionary**

import pandas as pd
df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}


# 💻 Project – NATO Alphabet Converter

Goal:
Convert a user’s name into a list of NATO phonetic alphabet words.

Example:
Enter your name: Deb

Output: ['Delta', 'Echo', 'Bravo']

📂 Folder Structure
day-26-nato-alphabet/

├── main.py # Main program logic

├── nato_phonetic_alphabet.csv # CSV data source

🚀 How to Run
1.	Clone the repository

git clone https://github.com/<your-username>/Day26.git
cd Day26
2.	Install dependencies

pip install pandas

3.	Run the program

python main.py


# 🛠 Skills Learned

•	List comprehension

•	Dictionary comprehension

•	Extracting and transforming CSV data with Pandas

•	Mapping user input to structured output
