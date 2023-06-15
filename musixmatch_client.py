from musixmatch import Musixmatch

from config import MUSIXMATCH_API_KEY


class MusixMatchClient:
    def __init__(self):
        self.musixmatch = Musixmatch(apikey=MUSIXMATCH_API_KEY)

    def get_lyrics(self, track: str, artist: str) -> str:
        response = self.musixmatch.matcher_lyrics_get(
            q_track=track,
            q_artist=artist
        )
        return response["message"]["body"]["lyrics"]["lyrics_body"]
