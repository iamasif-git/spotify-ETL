import sqlite3
from extract import DATABASE_CONNECTION
import transform
import sqlalchemy


df = transform.send_to_load()

engine = sqlalchemy.create_engine(DATABASE_CONNECTION)
conn = sqlite3.connect("mysongs.sqlite")
cursor = conn.cursor()

query = """
CREATE TABLE IF NOT EXISTS my_played_tracks (
song_name VARCHAR(100),
artist VARCHAR(100),
played_at(VARCHAR(100),
timestamp VARCHAR(100),
CONSTRAINT primary_key_constraint PRIMARY KEY (played_at) 
);
"""
cursor.execute(query)