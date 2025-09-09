# Day48 - Selenium Practice & Cookie Clicker Bot 🕹️🍪

## 📖 Overview
Day 48 of the 100 Days of Code challenge was all about **web scraping and automation** using the **Selenium** Python module.  
I practiced extracting data, interacting with web elements, and finally built a capstone project — an automated **Cookie Clicker Bot**.

---

## 📂 Project Structure
Day48/

│── Cookie Clicker Python Bot/

│ ├── main.py # Practice: Scraping Amazon & Python.org

│ ├── Challenge.py # Scraping Python.org upcoming events

│ ├── interaction.py # Automating a signup form

│ ├── cookie_clicker_bot_app.py # Capstone: Cookie Clicker Bot

---

## 🛠️ Concepts Learned
- Using Selenium to launch and control Chrome
- Locating elements:
  - `By.ID`, `By.NAME`, `By.CLASS_NAME`
  - `By.XPATH`, `By.CSS_SELECTOR`
- Extracting attributes & text from elements
- Sending keystrokes and form submissions
- Building structured dictionaries from scraped lists
- Handling exceptions with `NoSuchElementException`
- Writing automation loops with `time` & `sleep`

---

## 📜 Scripts

### 🔹 main.py (Practice)
- Scrapes product price from Amazon  
- Extracts elements like search bar, placeholder text, and links from Python.org  

### 🔹 Challenge.py
- Scrapes **dates & event names** from Python.org  
- Builds them into a dictionary `{index: {time, name}}`

### 🔹 interaction.py
- Auto-fills a signup form with name & email  
- Clicks the submit button  

### 🔹 cookie_clicker_bot_app.py (Capstone)
- Opens Cookie Clicker game  
- Continuously clicks the big cookie  
- Automatically buys best available upgrades  
- Runs for 5 minutes and shows final cookie count  

---

## 🚀 How to Run
1. Install requirements:
   ```bash
   pip install selenium
Download and set up ChromeDriver compatible with your Chrome version.
```

Run any script:

python main.py
python Challenge.py
python interaction.py
python cookie_clicker_bot_app.py

```

## 🎯 Key Takeaway
Selenium is not just for scraping static data — it’s powerful enough to automate complex web interactions. From filling forms to playing games, the possibilities are endless!

