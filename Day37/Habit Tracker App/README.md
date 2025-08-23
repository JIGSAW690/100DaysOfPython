# 🚴 Habit Tracker App (Pixela API)

This project is part of **Day 37 of 100 Days of Python**.  
The Habit Tracker App uses the [Pixela API](https://pixe.la/) to visualize daily habits such as cycling, coding, workouts, etc.  

---

## 🚀 Features
- Creates a **user** and **graph** on Pixela (if not already present)  
- Prompts user: *"How many kilometers did you cycle today?"*  
- Posts a **pixel** on the graph representing the daily activity  
- Supports updating and deleting pixels via Pixela endpoints  

---

## 🛠️ Tech Stack
- **Python 3**  
- `requests` → To communicate with Pixela REST API  
- `datetime` → To format dates as `YYYYMMDD` for API requests  
- `os` → To manage sensitive values like Pixela token and username via environment variables  

---

## 📂 Project Structure

Day37/

│── HabitTracker/

│ │── main.py # Main script to post/update/delete pixels

│── README.md # Documentation


---

## 🔑 Environment Variables

Before running the app, set the following environment variables:

```bash
export PIXELA_USERNAME="your_pixela_username"
export PIXELA_TOKEN="your_pixela_token"
export GRAPH_ID="graph1"
```

▶️ How to Run
Clone the repo and navigate to Day37 folder

Install dependencies:

pip install requests
Set up your environment variables (see above)

Run the script:

python main.py
📊 Example Output
When you run the script:

How many kilometers did you cycle today? 12

✅ Pixel posted successfully on Pixela graph!
Your activity will then be visible on the graph:

👉 View My Graph


***🔒 Security Note***

All sensitive data (Pixela token, username, graph ID) are stored as environment variables.
This avoids hardcoding secrets into the script, following DevOps best practices.