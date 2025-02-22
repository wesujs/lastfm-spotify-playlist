import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

LASTFM_API_KEY = os.getenv("LASTFM_API_KEY")
LASTFM_USER = os.getenv("LASTFM_USER")
SPOTIFY_CID = os.getenv("SPOTIFY_CID")
SPOTIFY_SECRET = os.getenv("SPOTIFY_SECRET")
SPOTIFY_REDIRECT_URI = "http://localhost:8888/callback"  # Must match Spotify dashboard
