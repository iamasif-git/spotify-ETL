import sqlite3
from extract import DATABASE_CONNECTION
import transform
import sqlalchemy


df = transform.send_to_load()

engine = sqlalchemy.create_engine(DATABASE_CONNECTION)
conn = sqlite3.connect("mysongs.db")
cursor = conn.cursor()

query = """
CREATE TABLE IF NOT EXISTS my_played_tracks(
song_name VARCHAR(100),
artist_name VARCHAR(100),
played_at VARCHAR(100) PRIMARY KEY,
timestamp VARCHAR(100)
);
"""

cursor.execute(query)
print("Opened Database connection")


try:
    df.to_sql("my_played_tracks",engine,index=False,if_exists='append')
except:
    print("data already exists in database")    
    
conn.close()
print("Connection closed")    