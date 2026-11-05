""" writes the fake data for replacement of Spotify's personal info 

* follows the same format as Spotify's real "Download your data" export

114K Spotify Tracks Dataset

This is fake data for the time being while it takes Spotify up to 30 days to deliver the real personal data

The fake listener has HIDDEN, and KNOWN habits
--> applied methods allow me to check if the algorithms are correct

Outputs:
    "streaming_history_audio_<year>_0.json" == real data from spotify

    "streaminghistory_music_0.json" == standard account data 

"""

import argparse
import json
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo
 
import numpy as np
import pandas as pd
 
AUDIO_COLS = ["danceability", "energy", "valence", "tempo", "acousticness",
              "instrumentalness", "speechiness", "loudness", "liveness"]

PERSONA = {
    "morning" : {"hours": range(6, 11), "genres": {"acoustic": 3, "chill": 3, "indie":2, "piano":1}},
    "afternoon": {"hours": range(11, 17), "genres": {"pop":3, "indie":2, "r-n-b":2, "rock":1}},
    "evening": {"hours": range(17, 22), "genres": {"hip-hop": 3, "edm": 2, "pop": 2, "r-n-b": 1}},
    "late_night": {"hours": list(range(22, 24)) + list(range(0, 6)), "genres": {"chill": 3, "study": 2, "ambient": 2, "sleep": 1}},

}

# how most sessions start at each hour 
HOUR_START = np.array([1, 0.5, .3, .2, .2, .3, 1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 3, 4, 3, 2, 1.5, 1.5, 1.5, 1.5],dtype=float)