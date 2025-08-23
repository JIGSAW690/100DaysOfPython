# Day 25 – Pandas & Data Analysis Projects

## 📌 Overview
Today's session focused on learning **Pandas** for data analysis in Python.  
I explored how to:
- Read CSV files into Pandas DataFrames
- Use Series functions like `max()`, `min()`, `mean()`, `median()`, etc.
- Extract specific columns and rows based on conditions
- Create a DataFrame from scratch using lists or dictionaries
- Export processed data back to CSV files

After mastering the basics, I built **two data projects**.

---

## 🐿 Project 1 – Squirrel Census Data Analysis
**Dataset:** 2018 Central Park Squirrel Census

**Goal:**  
Count the number of squirrels by fur color (**Cinnamon**, **Black**, **Gray**) and export the results into a new CSV file.

**Files & Folders:**

day-25-start/

├── 2018_Central_Park_Squirrel_Census_-_Squirrel_Data_202508.csv   # Original dataset

├── main.py                                                        # Pandas basics & CSV processing

├── squirrel.py                                                    # Squirrel data analysis logic

├── squirrel_data.csv                                              # Output: squirrel color counts

├── Students.csv                                                   # Practice dataset

├── weather_data.csv                                               # Practice dataset

---

## 🇺🇸 Project 2 – U.S. States Game App
**Modules used:**  
- `turtle` for graphics  
- `pandas` for data handling  

**Goal:**  
Interactive game that:
- Displays a blank U.S. map
- Prompts the user to guess state names
- Marks correct guesses on the map
- Ends when all 50 states are guessed or when the user types `Exit`
- Saves the remaining states to a CSV file

**Files & Folders:**

day-25-us-states-game-start/

├── 50_states.csv              # State names & coordinates

├── blank_states_img.gif       # U.S. map background

├── main.py                    # Game logic

├── States_Left_to_know.csv    # Output: states not guessed


---

## 🚀 How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/<your-username>/Day25.git
   cd Day25
2.	Install dependencies:
pip install pandas
3.	Run Squirrel Census Project:
cd day-25-start
python squirrel.py
4.	Run U.S. States Game:
cd day-25-us-states-game-start
python main.py


📊 Output Samples

•	Squirrel Census: CSV file with squirrel counts by color

•	US States Game: Updated U.S. map with guessed states + CSV of missed states
________________________________________
🛠 Skills Learned

•	Data extraction, transformation, and analysis with Pandas

•	Creating and modifying DataFrames

•	Exporting processed data to CSV

•	Using turtle for interactive graphical applications
