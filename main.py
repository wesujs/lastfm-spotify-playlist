from lastfm.lastfm_api import get_lastfm_top_tracks
from spotify.spotify_api import search_song_on_spotify, create_spotify_playlist, add_songs_to_playlist
from utils.env_loader import LASTFM_USER
import time

def main():
    """Main execution function"""
    print("Fetching top Last.fm tracks...")
    top_songs = get_lastfm_top_tracks()

    print("Searching for songs on Spotify...")
    track_ids = []
    missing_tracks = []  # Store missing songs

    for song, artist in top_songs:
        track_id = search_song_on_spotify(song, artist)
        if track_id:
            track_ids.append(track_id)
        else:
            missing_tracks.append(f"{song} by {artist}")  # Keep track of missing songs
        time.sleep(0.5)  # Avoid hitting rate limits

    if not track_ids:
        print("No valid songs found on Spotify.")
        return

    print("Creating Spotify playlist...")
    playlist_name = f"Top Songs Ever ({LASTFM_USER})"
    playlist_id = create_spotify_playlist(playlist_name)

    print("Adding songs to playlist...")
    add_songs_to_playlist(playlist_id, track_ids)

    print("Playlist created successfully!")

    if missing_tracks:
        print("\nThe following tracks could not be found on Spotify:")
        for track in missing_tracks:
            print(f"- {track}")

if __name__ == "__main__":
    main()
