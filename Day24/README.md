# 📂 Day 24 – File Handling in Python

Today’s challenge focused on **reading from, writing to, and appending to files** in Python using the `with open()` function.

---

## 📌 Part 1 – Snake Game Upgrade 🐍
We enhanced the **Day 21 Snake Game** by:
- Adding a **Highest Score** feature.
- Saving the score in a `data.txt` file.
- Ensuring the high score **persists** even after the game is closed and reopened.

### Implementation Highlights
- Used:
  ```python
  with open("data.txt", mode="r") as file:
      contents = file.read()


•	Updated file only when a new high score was reached.
________________________________________
📌 Part 2 – Mail Merger Project ✉️

Created a script that automatically personalizes letters for multiple recipients.

Project Structure
Day24/
│
├── Input/
│   ├── Letters/
│   │   └── starting_letter.txt
│   └── Names/
│       └── invited_names.txt
│
├── Output/
│   └── ReadyToSend/
│
└── main.py

Steps:
1.	Read the template letter.
2.	Read the names list.
3.	Replace the placeholder name in the template for each recipient.
4.	Save each personalized letter in the Output/ReadyToSend folder.
🛠 Technologies Used
•	Python 3.x
•	File Handling (open, read, write)
________________________________________
▶️ How to Run
1.	Clone the repo:
git clone https://github.com/debkankan/100DaysOfPython.git

2. cd 100DaysOfPython/Day24
2.	Run the program:
python main.py
🙌 Acknowledgments

Inspired by Angela Yu’s 100 Days of Code: The Complete Python Bootcamp
