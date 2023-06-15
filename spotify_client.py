import spotipy
from spotipy.oauth2 import SpotifyOAuth

from config import (SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET,
                    SPOTIPY_REDIRECT_URI)


class SpotifyClient:
    def __init__(self):
        scope = "user-read-private,playlist-read-private"
        auth_manager = SpotifyOAuth(
            client_id=SPOTIPY_CLIENT_ID,
            client_secret=SPOTIPY_CLIENT_SECRET,
            redirect_uri=SPOTIPY_REDIRECT_URI,
            scope=scope
        )
        self.sp = spotipy.Spotify(auth_manager=auth_manager)

    @property
    def username(self) -> str:
        current_user = self.sp.current_user()
        return current_user["id"]

    def get_playlists(self) -> list:
        return self.sp.user_playlists(self.username)["items"]

    def get_tracks_from_playlist(self, playlist_id: int) -> list:
        response = self.sp.playlist_tracks(playlist_id=playlist_id)
        return response["items"]
