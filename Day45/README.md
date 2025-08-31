# Day45 - Web Scraping with BeautifulSoup

This project is part of my **100 Days of Code** journey (Day 45).  
The main focus was learning **web scraping** using the `bs4` (BeautifulSoup) library in Python.

---

## 📖 Learnings
- Introduction to the **BeautifulSoup class** from `bs4` module.
- Parsing local HTML files into Python as a **Soup object**.
- Extracting tags, attributes, and text (`.find()`, `.find_all()`, `.select()`, etc.).
- Understanding **legal vs illegal** aspects of web scraping.
- Using **environment variables** for security (instead of hardcoding URLs).

---

## 📂 Project Structure
Day45

┣ b64_start

┃ ┣ local_website.py # Scraping from local HTML (website.html)

┃ ┣ main.py # Scraping from Hacker News

┃ ┗ website.html # Local test HTML page

┣ scrape_movie

┃ ┣ main.py # Scraping Empire Online movie list

┃ ┗ movies.txt # Output file with movie names

---

## 🛠️ Code Walkthrough

### 1. Local Website Scraping (`local_website.py`)
- Loaded a **local HTML file** (`website.html`) into BeautifulSoup.
- Extracted:
  - Title, headings, and anchor tags.
  - Text and attributes (`href`) from `<a>` tags.
  - Specific elements by `id`, `class`, and CSS selectors.

### 2. Live Website Scraping (`main.py` in `b64_start`)
- Scraped **Hacker News** (`https://news.ycombinator.com/news`).
- Extracted:
  - Article titles  
  - Links  
  - Upvotes

### 3. Final Project (`main.py` in `scrape_movie`)
- Scraped **Empire Online’s Best Movies list** (`https://www.empireonline.com/movies/features/best-movies-2/`).
- Extracted all movie titles.
- Wrote them into `movies.txt` in **reverse order**.
- Used **environment variable (`MOVIES_ENDPOINT`)** for the URL.

---

## 🚀 How to Run
1. Clone/download the repo.  
2. Install dependencies:
   ```bash
   pip install beautifulsoup4 lxml requests
   ```
Set your environment variable:

export MOVIES_ENDPOINT="https://www.empireonline.com/movies/features/best-movies-2/"

Run the scripts:

python local_website.py

python main.py   # for Hacker News

python scrape_movie/main.py

## 📌 Notes
Web scraping legality: Always check robots.txt and site’s ToS before scraping live websites.

This project was purely for learning purposes.

## ✅ Output Example
For the movie scraper, movies.txt contains:

markdown
Copy code
1. Movie Name
2. Movie Name
...
100. Movie Name

## Day45 Summary
Learned how to convert web pages into data pipelines with Python. A really powerful skill for data collection and automation.