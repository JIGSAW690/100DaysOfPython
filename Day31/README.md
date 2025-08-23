Readme: 

# 📚 Flash Card Project (Day 31)

A flash card application built with **Python Tkinter**, **Pandas**, and **Random** module to help users learn French-to-English translations. 
The app dynamically adapts to user progress, ensuring efficient vocabulary learning.

---

## 🚀 Features
- Displays a **French word** first.
- Automatically flips to the **English translation** after **3 seconds**.
- ✅ **Known words** are removed from the learning set (`words_to_learn.csv`).
- ❌ **Unknown words** stay in the dataset for future practice.
- Persists user progress across sessions.
- Can easily be adapted for other language pairs by swapping the CSV input file.

---

## 🗂️ Project Structure
Day31/

└── flash-card-project-start/

├── data/

│   ├── french_words.csv       # Original dataset

│   └── words_to_learn.csv     # Created/updated dynamically after ✅ clicks


├── images/

│   ├── card_back.png          # Card back design (English word)

│   ├── card_front.png         # Card front design (French word)

│   ├── right.png              # ✅ Button image

│   └── wrong.png              # ❌ Button image

├── main.py                    # Main application code

└── README.md                  # Project documentation


---

## 🖥️ How It Works
1. Run `main.py`.
2. A **French word** will appear.
3. After **3 seconds**, the card flips to show the **English translation**.
4. ✅ If you know the word → it is removed from the dataset. 
❌ If not → it stays for future revision.
5. The app will automatically create/update `words_to_learn.csv` to track your progress.

---

## 📦 Dependencies
- Python 3.x
- Tkinter
- Pandas

Install required packages:
```bash
pip install pandas
```

**🎯 Learning Outcomes**

•	GUI design with Tkinter

•	Handling timed events (after method)

•	Data persistence using CSV and Pandas

•	Implementing user-driven adaptive learning systems
________________________________________
**🌍 Future Improvements**

•	Add multiple language support in a single app.

•	Track session stats (e.g., words learned per session).

•	Add sound for pronunciation.
