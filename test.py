import sys
from os import getenv as env
import mysql.connector
from mysql.connector import cursor
from datetime import datetime
sys.path.append('.')

from dotenv import find_dotenv, load_dotenv

ENV_FILE = find_dotenv()

if ENV_FILE:
    load_dotenv(ENV_FILE)


mydb = mysql.connector.connect(
    host=env('DB'),
    port=env('DB_PORT'),
    user=env('DB_USER'),
    password=env('DB_PASSWORD')
)

corona_cursor = mydb.cursor()
corona_cursor.execute("USE DailyCode")


#corona_cursor.execute("truncate CoronaData")
mydb.commit()
print("deleted all data!!!")