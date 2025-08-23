# Day 28 – Pomodoro Timer App ⏳🍅

## 📌 Overview
A **Pomodoro Timer** built with Python's **Tkinter** GUI library and the **math** module to track focused work sessions and breaks.

This app implements the popular **Pomodoro Technique**:
- **25 min work**
- **5 min break**
- Repeat for 4 cycles, then take a **20 min long break**
- Visual checkmarks show completed work sessions
- **Reset button** to return to the initial state

---

## 🖼 Features
- **Start Button** → initiates the Pomodoro cycle.
- **Timer Display** → shows countdown for work/break sessions.
- **Checkmark Counter** → one checkmark for each completed work session.
- **Reset Button** → clears timer and progress.
- **Tomato Image** for a friendly, themed interface.

---

## 🔄 Logic Flow
Start → Work (25 min) → Short Break (5 min) → Work (25 min) → Short Break (5 min)
→ Work (25 min) → Short Break (5 min) → Work (25 min) → Long Break (20 min) → Repeat
- 1 ✅ checkmark appears after each 25 min work session.
- No checkmarks by default; they accumulate as work sessions complete.

---

## 📂 Project Structure
Day28/

└── pomodoro-start/

├── main.py        # Application logic & Tkinter UI

├── tomato.png     # Themed image asset for the UI

---

## 🚀 How to Run
1. **Clone the repository**
```bash
git clone https://github.com/<your-username>/Day28.git
cd Day28/pomodoro-start

2.	Run the application
python main.py
```

## 🛠 Skills Learned
•	Tkinter UI building

•	Event-driven programming

•	Using after() for countdown timers

•	Dynamic widget updates in Tkinter

•	Structuring productivity tools in Python
