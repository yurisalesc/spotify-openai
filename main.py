from openai_client import OpenAIClient
from spotify_client import SpotifyClient
from vagalume_client import VagalumeClient

openai = OpenAIClient()
spotify = SpotifyClient()
vagalume = VagalumeClient()


def display_formatted_data(artist: str, track: str, sentiment: str) -> None:
    print('---------------------------------------------------------')
    print(f"Artist: {artist}\nTrack: {track}\nSentiment: {sentiment}")


def display_sentiments_for_playlist_tracks(tracks: list) -> None:
    for track_info in tracks:
        track_info = track_info["track"]
        track, artist = track_info["name"], track_info["artists"][0]["name"]

        lyrics = vagalume.get_lyrics(track=track, artist=artist)

        sentiment = openai.classify_sentiment(lyrics=lyrics)

        display_formatted_data(artist=artist, track=track, sentiment=sentiment)


playlists = spotify.get_playlists()
playlists = playlists[::1]

for playlist in playlists:
    print(f"\n====================={playlist['name']}=====================")
    tracks = spotify.get_tracks_from_playlist(playlist_id=playlist["id"])
    display_sentiments_for_playlist_tracks(tracks=tracks)
