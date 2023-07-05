from openai_client import OpenAIClient
from spotify_client import SpotifyClient
from vagalume_client import VagalumeClient


class TrackSentimentClassifier:
    def __init__(self):
        self.openai = OpenAIClient()
        self.spotify = SpotifyClient()
        self.vagalume = VagalumeClient()

    def get_playlists(self):
        playlists = self.spotify.get_playlists()
        return playlists[::1]

    def get_tracks_from_playlist(self, playlist_id: str) -> list:
        return self.spotify.get_tracks_from_playlist(playlist_id=playlist_id)

    def get_track(self, payload: dict) -> str:
        return payload["track"]["name"]

    def get_artist(self, payload: dict) -> str:
        return payload["track"]["artists"][0]["name"]

    def get_track_lyrics(self, payload: dict):
        track = self.get_track(payload=payload)
        artist = self.get_artist(payload=payload)
        print(f"\ntrack: {track}, artist: {artist}")
        return self.vagalume.get_lyrics(track=track, artist=artist)

    def get_classification(self, lyrics: str) -> str:
        return self.openai.classify_sentiment(lyrics=lyrics)


if __name__ == "__main__":
    track_classifier = TrackSentimentClassifier()

    playlists = track_classifier.get_playlists()
    for playlist in playlists:
        tracks = track_classifier.get_tracks_from_playlist(
            playlist_id=playlist["id"]
        )
        for track_info in tracks:
            lyrics = track_classifier.get_track_lyrics(payload=track_info)
            sentiment = track_classifier.get_classification(lyrics=lyrics)
            print(sentiment)
