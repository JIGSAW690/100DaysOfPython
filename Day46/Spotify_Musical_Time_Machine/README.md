# 🎶 Spotify Musical Time Machine  

A Python project that lets you travel back in time and recreate the **Billboard Top 100 songs** of any given date—right inside your **Spotify account**.  

---

## 🚀 Features  
- Enter any date in the format `YYYY-MM-DD`.  
- Fetches the Billboard Top 100 songs for that date using **web scraping**.  
- Creates a **private Spotify playlist** in your account with those songs.  
- Automatically skips unavailable songs.  

---

## 🛠️ Tech Stack  
- **Python**  
- [BeautifulSoup (bs4)](https://pypi.org/project/beautifulsoup4/) → For parsing Billboard charts  
- [Requests](https://pypi.org/project/requests/) → To fetch HTML content  
- [Spotipy](https://spotipy.readthedocs.io/) → For Spotify API integration  
- **os** → For handling environment variables  

---

## 📂 Project Structure  
Spotify_Musical_Time_Machine/

│── main.py # Main script to run the project

│── token.txt # Stores Spotify API authentication token

---

## ⚙️ Setup Instructions  

1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/Spotify_Musical_Time_Machine.git
   cd Spotify_Musical_Time_Machine
   ```
## Install dependencies:

pip install -r requirements.txt
Set up environment variables (in your terminal or .env file):

export MY_BROWSER_HEADER="your_browser_user_agent"
export BILLBOARD_ENDPOINT="https://www.billboard.com/charts/hot-100/"
export CLIENT_ID="your_spotify_client_id"
export CLIENT_SECRET="your_spotify_client_secret"
export USERNAME="your_spotify_username"

## Run the project:

python main.py

Enter the date in the format YYYY-MM-DD (example: 2000-08-15).

The script will fetch songs from Billboard.

It will create a Spotify playlist with those songs.

## 🎯 Example

Which year do you want to travel to? Type the date in the format YYYY-MM-DD: 2005-05-20

✅ Playlist created: "2005-05-20 Billboard 100"

## 📌 Notes
Playlist is private by default.

Some songs may not exist on Spotify and will be skipped.

## 📜 License
This project is for learning & educational purposes.