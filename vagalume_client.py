import requests

from settings import VAGALUME_API_KEY


class VagalumeClient:
    def __init__(self):
        self.url = "https://api.vagalume.com.br/search.php?"

    def get_lyrics(self, track: str, artist: str) -> str:
        query = f"art={artist}&mus={track}&apikey={VAGALUME_API_KEY}"
        url = self.url + query
        response = requests.get(url)

        try:
            lyrics = response.json()["mus"][0]["text"]
            return lyrics.replace("\n", " ").strip()
        except KeyError:
            return ""
