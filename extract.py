from calendar import c
import requests
import sqlite3
import pandas as pd
import datetime
import sqlalchemy
import json


DATABASE_CONNECTION = "sqlite://mysongs.db"
TOKEN = "BQBj_WimzdynckHmV0bIrL-IE9fOSNZ7wzkp9gimxnkL-czbovGEN3dI1Jfkyht9ZmyCs_8_4z-caGyOiqzTQOmnxt0h6VhaFQwAyzLFxHdGe2Rolyvy559odFYObX3fRz0GXs8UTa9YoV3GtNWtwnEV_HZUsvcRTKdKBZU0Aag9HpyiNbJVODBh2pEKAb2JihLgAq4yDeN4TA"
USER_ID = "MD ASIF"

header = {
    "Accept":"Application/json",
    "Content-Type":"Application/json",
    "Authorization":"Bearer {token}".format(token=TOKEN)
}
song_name = []
artist_name = []
played_at = []
time_stamp = []
today = datetime.datetime.now()
#print(today)
yesterday = today - datetime.timedelta(days=1)
#print(yesterday)
yesterday_unix_timestamp = int(yesterday.timestamp())*1000
#print(yesterday_unix_timestamp)
today_unix_timestamp = int(today.timestamp())*1000

response = requests.get("https://api.spotify.com/v1/me/player/recently-played?after={time}".format(time=yesterday_unix_timestamp),headers=header)
response = response.json()

def songs_extract():
    song_name = []
    artist_name = []
    played_at = []
    time_stamp = []

    for item in response['items']:
        song_name.append(item['track']['name'])
        artist_name.append(item['track']['artists'][0]['name'])
        played_at.append(item['played_at'])
        time_stamp.append(item['played_at'][0:10])

    data = {
        "song name":song_name,
        "artist name":artist_name,
        "played at":played_at,
        "timestamp": time_stamp
    }

    songs_df = pd.DataFrame(data)
    return(songs_df)


        