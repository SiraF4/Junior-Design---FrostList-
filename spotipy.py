import spotipy
from spotipy.oauth2 import SpotifyOAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="YOUR_ID", client_secret="YOUR_SECRET",
    redirect_uri="http://127.0.0.1:8888/callback",
    scope="user-read-recently-played playlist-modify-private"))
recent = sp.current_user_recently_played(limit=50)

import pandas as pd
df = pd.read_csv("dataset.csv")
df = df.dropna(subset=["track_name", "artists"])
df = df.drop_duplicates(subset=["track_id"])

from rapidfuzz import process, fuzz
key = f"{song} {artist}".lower()
match, score, idx = process.extractOne(key, df["search_key"], scorer=fuzz.token_sort_ratio)
if score > 90: features = df.iloc[idx]

plays = plays.sort_values("played_at")
gap = plays["played_at"].diff() > pd.Timedelta(minutes=30)
plays["session_id"] = gap.cumsum()
sessions = plays.groupby("session_id")["cluster"].apply(list)