from email import header
from wsgiref import headers
import requests
import sqlalchemy
import pandas as pd
from sqlalchemy.orm import sessionmaker
import datetime
import sqlite3


DATABASE_CONNECTION = 'sqlite://my_user_info.db'
USER_ID = "MD ASIF"
TOKEN = "BQDnoJNP_m6ClW2JX24dnivJCfOlqC5HEpUX7ReKK7FeAk3uMiuaAXPJ3ulgIOI-CqAdae4ViPEVMju38eBU8p4xpKWsNvSJCfKQ60txAmrqr_wXa32jq9HZ5yGpX2Iojy9kn_-imgJAiWUIjp7bIDEbtOj_IH7c-6emnd8hCHrIDhOnaz7iWHziRFhBcj_4UaYvxmdquqg"


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

user_info = {
"country":response['country'],
"user name": response['display_name'],
"email": response['email']
}
print(user_info)
user_df = pd.DataFrame([user_info]) 
print(user_df)