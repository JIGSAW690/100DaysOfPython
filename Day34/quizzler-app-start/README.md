 # 🧠 Day 34 Project - GUI Quiz App with Tkinter

This project is an upgraded version of the **Day 17 Quiz App**. 
Instead of a console-based quiz, this version has a **Graphical User Interface (GUI)** built with **Tkinter** and fetches **live questions from an API**.

---

## 🚀 Features
- Fetches **10 random True/False questions** from the [Open Trivia DB](https://opentdb.com/api.php)
- GUI built with **Tkinter**
- ✅ / ❌ buttons to answer (True or False)
- **Visual feedback**:
- Green highlight → Correct Answer
- Red highlight → Wrong Answer
- **Score tracking**:
- Updates in real-time on the top-right corner
- Starts at 0 and increases with correct answers
- **Game End Handling**:
- After 10 questions → "End of Quiz" message appears
- Buttons are automatically disabled

---

## 🗂️ Project Structure

quizzer-app-start/

├── images/

│   ├── false.png        # Button image for ❌

│   └── true.png         # Button image for ✅

├── data.py              # Fetches question data from API

├── main.py              # Entry point (runs the game)

├── question_model.py    # Defines Question class

├── quiz_brain.py        # Game logic (questions, score, progression)

├── ui.py                # Tkinter UI (canvas, buttons, labels)

├── type_hint.py         # Notes / type hint examples

└── README.md

---

## ⚙️ How It Works
1. **Start the game** → Run `main.py`
2. A **Tkinter window** opens with a score label, canvas for questions, and ✅/❌ buttons
3. User selects an answer:
- Correct → canvas turns **green** for 1 second
- Wrong → canvas turns **red** for 1 second
4. After 10 questions:
- Canvas displays **"End of Quiz"**
- Both buttons are disabled

---

## 🛠️ Tech Stack
- **Python Modules**:
- `tkinter` → GUI
- `requests` → API calls
- `time` & `after()` method → timing visual feedback
- **API**: [Open Trivia DB](https://opentdb.com/api.php)

---

## 🎯 Learning Outcomes
- Using **Tkinter** to build interactive GUIs
- Fetching live data from **APIs**
- Applying **OOP concepts** in structuring projects
- Managing **real-time feedback and user interaction**

---

## 🌟 Future Improvements
- Add category & difficulty selection before starting the quiz
- Support for multiple-choice questions
- Save high scores locally
- Dark mode theme for UI
