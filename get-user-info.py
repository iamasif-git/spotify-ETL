from email import header
from logging import exception, raiseExceptions
from re import L
from tkinter import E
from wsgiref import headers
import requests
import sqlalchemy
import pandas as pd
from sqlalchemy.orm import sessionmaker
import datetime
import sqlite3


DATABASE_CONNECTION = 'sqlite://my_user_info.db'
USER_ID = "MD ASIF"
TOKEN = "BQB6FAMCzRfsxqTSTppBaHptGGzYx1YT4vsu4Yg81mAhcYrbVDebstWqyhtWkHPwHB_vI4WUpW9w-Z6zejUD2oUTw9pNqcEdju5uHUnbN6zqVp_K5Zplo2qzOXggnuUkUGowmxQN61OpZGh_F4mH-PzTzjOB58_D5a9qa4Tl8Ja8iT8sKRa_rLDpX1LP-KMdKVk"


user_header =  {
    "Accept":"application/json",
    "content-type":"application/json",
    "Authorization":"Bearer {token}".format(token=TOKEN)
}

today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days = 1)
yesterday_unix_timestamp = int(yesterday.timestamp())*1000

response = requests.get("https://api.spotify.com/v1/me?after={time}".format(time=yesterday_unix_timestamp),headers=user_header)


response=response.json()
#print(response)
user_info = {
"user name": response['display_name'],
"email": response['email']
}

user_df = pd.DataFrame([user_info])

#Data validation
def dataframeChecks(user_df:pd.DataFrame):
    if (user_df.empty()):
        print("No user found")
        return False

    if(user_df['email'].is_unique()):
        pass
    else:
        raise Exception ("Primary key check violated") 

    if (user_df.isnull()):
        raise Exception ("Null Value Found")

if(dataframeChecks(user_df)):
    print("Data valid. Proceed with Loading")

    




print(user_df)