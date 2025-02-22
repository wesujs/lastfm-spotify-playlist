import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
from utils.env_loader import SPOTIFY_CID, SPOTIFY_SECRET, SPOTIFY_REDIRECT_URI

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CID,
    client_secret=SPOTIFY_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="playlist-modify-public"
))

def search_song_on_spotify(song_name, artist_name):
    """Search for a song on Spotify and return its track ID"""
    query = f"track:{song_name} artist:{artist_name}"
    results = sp.search(q=query, type="track", limit=1)
    return results["tracks"]["items"][0]["id"] if results["tracks"]["items"] else None

def create_spotify_playlist(name):
    """Create a new playlist on Spotify"""
    user_id = sp.current_user()["id"]
    playlist = sp.user_playlist_create(user=user_id, name=name, public=True)
    return playlist["id"]

def add_songs_to_playlist(playlist_id, track_ids):
    """Add songs to the new Spotify playlist"""
    if track_ids:
        sp.user_playlist_add_tracks(user=sp.current_user()["id"], playlist_id=playlist_id, tracks=track_ids)
