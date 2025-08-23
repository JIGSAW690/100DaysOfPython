# Day 27 – *args, **kwargs & Tkinter GUI Development

## 📌 Overview
Today's learning was divided into two major parts:
1. Function flexibility with `*args` & `**kwargs`
2. Building graphical user interfaces (GUI) using the Tkinter library

---

## 📝 Topics Covered ##

## 1️⃣ *args & **kwargs ##
- **`*args`** allows a function to take any number of positional arguments.
- **`**kwargs`** allows a function to take any number of keyword arguments.

Example:
```python
def demo_function(*args, **kwargs):
    print(args)      # tuple of positional arguments
    print(kwargs)    # dictionary of keyword arguments

demo_function(1, 2, 3, name="Deb", role="DevOps")
# Output:
# (1, 2, 3)
# {'name': 'Deb', 'role': 'DevOps'}
Practice file: playground.py
```

## 2️⃣ Tkinter Module ##

Tkinter is Python’s built-in library for creating GUIs.

Placement Managers:
•	pack() – simple, stacks widgets vertically/horizontally
•	place() – precise positioning using x & y coordinates
•	grid() – table-like row & column placement

Practice files:
•	tkinter_widgets.py
•	tkinter_grid.py
________________________________________
## 💻 Project – Miles to Kilometer Converter

Goal: Convert miles to kilometers with a simple, interactive GUI.

Features:
•	Input field for miles

•	“Convert” button

•	Output label showing kilometers

Formula:
km = miles × 1.60934

Example:

Enter miles: 10

Output: 16.09 km


📂 Folder Structure

day-27-tkinter-converter/

├── playground.py         # *args and **kwargs practice

├── tkinter_widgets.py    # Tkinter basics

├── tkinter_grid.py       # Tkinter grid layout example

├── main.py               # Miles to Kilometer converter app

🚀 How to Run

1.	Clone the repository

git clone https://github.com/<your-username>/Day27.git
cd Day27

2.	Run the program

python main.py


## 🛠 Skills Learned
•	Flexible function arguments with *args & **kwargs

•	Building GUIs with Tkinter

•	Widget placement using pack, place, and grid

•	Handling user input and updating output dynamically

