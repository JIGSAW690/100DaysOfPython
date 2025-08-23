# 🐢 Turtle Crossing Game – Day 23 of #100DaysOfPython

A fun arcade-style game built using Python's Turtle module as part of the #100DaysOfPython challenge.  
In this game, the player controls a turtle that must cross a road filled with fast-moving cars without getting hit.

## 🎮 Gameplay Overview

- The player uses the **Up Arrow Key** to move the turtle upwards.
- Randomly generated cars move horizontally across the screen.
- Each time the turtle reaches the top (finish line), the game:
  - Resets the turtle's position.
  - Increases the **level**.
  - Speeds up the cars to increase difficulty.
- The game ends when the turtle **collides** with any car.
- The final score (level reached) is displayed with a **Game Over** prompt.

## 🧱 Object-Oriented Structure

The project is modular and uses classes for better separation of concerns:

### 📄 Files & Classes

- `main.py`: Core game loop and control logic.
- `player.py` → `Player` class: Controls turtle movement and reset logic.
- `car_manager.py` → `CarManager` class: Handles car creation, movement, and collision detection.
- `scoreboard.py` → `Scoreboard` class: Displays current level and game over screen.

## 🛠 Technologies Used

- Python 3.9.x
- Turtle Graphics module

## ▶️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/debkankan/100DaysOfPython.git
   cd 100DaysOfPython/Day23


Inspired by the curriculum from Angela Yu’s 100 Days of Code: The Complete Python Bootcamp
________________________________________
Happy Coding! 🚀
#Python #100DaysOfCode #TurtleGraphics #GameDev #PythonProjects
