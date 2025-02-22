# 🎵 Last.fm to Spotify Playlist Creator For Top 100 Songs

This project automatically **fetches the Top 100 songs from a Last.fm user's history** and creates a **Spotify playlist** with them.  
It retrieves scrobbles using the **Last.fm API** and searches for the songs in **Spotify**, adding them to a new playlist.

🚀 **A GUI and a web-based version of this program are currently in development! Stay tuned!**

---

## **🔗 API References**
- [🔗 Last.fm API - Get Your API Key](https://www.last.fm/api/)  
- [🔗 Spotify API - Create a Developer App](https://developer.spotify.com/dashboard/)  

---

## **🛠 Features**
✅ Fetches **Top 100** Last.fm tracks  
✅ Searches for songs on **Spotify**  
✅ Creates a **Spotify playlist** automatically  
✅ Skips missing songs and **logs unfound tracks**  
✅ **Future Updates:** GUI and Web App  

---

## **📂 Project Structure**
```
lastfm-spotify-playlist/
│── lastfm/             # Handles Last.fm API calls
│   │── __init__.py
│   │── lastfm_api.py
│
│── spotify/            # Handles Spotify API calls
│   │── __init__.py
│   │── spotify_api.py
│
│── utils/              # Handles environment variables
│   │── __init__.py
│   │── env_loader.py
│
│── .env                # Stores API keys (ignored in Git)
│── main.py             # Runs the script
│── README.md           # Documentation
│── requirements.txt     # Dependencies list
│── .gitignore          # Prevents pushing sensitive files
```

---

## **🚀 Getting Started**
### **1️⃣ Install Dependencies**
Clone the repository and install the required Python libraries:
```bash
git clone https://github.com/yourusername/lastfm-spotify-playlist.git
cd lastfm-spotify-playlist
pip install -r requirements.txt
```

---

### **2️⃣ Set Up API Keys**
Create a **`.env`** file in the project directory and add:
```
LASTFM_API_KEY=your_lastfm_api_key
LASTFM_USER=your_lastfm_username
SPOTIFY_CID=your_spotify_client_id
SPOTIFY_SECRET=your_spotify_client_secret
```

---

### **3️⃣ Run the Program**
To fetch your top Last.fm tracks and create a Spotify playlist, run:
```bash
python main.py
```

### **💡 How It Works**
1. Retrieves **Top 100 Last.fm songs**  
2. Searches for songs on **Spotify**  
3. Creates a **Spotify playlist**  
4. Shows **missing tracks** (if any)

---

## **🌟 Future Plans**
- **🖥 GUI Version** – A user-friendly graphical interface  
- **🌍 Web Version** – A hosted website for easy playlist creation  
- **🔎 Improved Search Matching** – Better song identification  

📢 **Follow the project for updates!** 🚀  

---
📝 **Made with ❤️ by Wes**
