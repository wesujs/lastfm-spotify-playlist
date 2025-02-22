import requests
from utils.env_loader import LASTFM_API_KEY, LASTFM_USER

def get_lastfm_top_tracks(limit=100):
    """Fetch top songs from Last.fm history"""
    url = f"http://ws.audioscrobbler.com/2.0/?method=user.getTopTracks&user={LASTFM_USER}&api_key={LASTFM_API_KEY}&format=json&limit={limit}"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error fetching Last.fm data:", response.status_code)
        return []

    data = response.json()
    return [(track["name"], track["artist"]["name"]) for track in data.get("toptracks", {}).get("track", [])]
