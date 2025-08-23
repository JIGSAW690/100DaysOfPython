# 🏓 Day 22 - Pong Game | 100 Days of Python

This project recreates the classic **Pong Game** using Python's `turtle` module and Object-Oriented Programming. It's a **2-player game**, where each player controls a paddle and tries to prevent the ball from passing their side.

---

## 🛠️ Technologies Used
- Python 3
- Turtle Graphics Module
- OOP (Classes, Methods, Encapsulation)
- Event Handling (Keyboard Listeners)

---

## 🚀 Features

- 🎮 Two-player paddle control (Left: `W`/`S`, Right: `Up`/`Down`)
- 🏓 Ball continuously moves and bounces off the top and bottom walls
- 🧠 Collision detection with paddles
- ❌ Miss detection when the paddle fails to hit the ball
- 🔁 Ball resets to center on a miss
- ⚡ Ball speed increases with each successful paddle hit
- 🧾 Scoreboard updates for both players

---

## 📁 File Structure

Day22/
│
├── main.py # Main game loop and orchestration
├── paddle.py # Paddle class for left and right paddles
├── ball.py # Ball class for movement and collisions
└── scoreboard.py # Scoreboard class for tracking and displaying scores
yaml
CopyEdit

---

## 🎮 How to Play

1. Clone the repo:
   ```bash
   git clone https://github.com/debkankan/100DaysOfPython.git
   cd Day22
2.	Run the game:
bash
CopyEdit
python main.py
3.	Controls:
o	Left Paddle: W (Up), S (Down)
o	Right Paddle: ↑ (Up), ↓ (Down)
________________________________________
📚 What I Learned
•	Creating interactive games using Turtle
•	Managing multiple classes for different game components
•	Handling real-time events using keyboard listeners
•	Implementing game logic like collision detection, scoring, and object movement
