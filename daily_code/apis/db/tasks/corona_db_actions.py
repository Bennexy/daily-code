import sys

import mysql.connector
from mysql.connector import cursor
from datetime import datetime
sys.path.append('.')
from daily_code.config import *
from daily_code.logger import get_logger

logger = get_logger('corona-db-actions')

mydb = mysql.connector.connect(
    host=DB,
    port=DB_PORT,
    user=DB_USER,
    password=DB_PASSWORD
)

corona_cursor = mydb.cursor()
corona_cursor.execute("USE DailyCode")




def check_for_entry(ort, orttype):
    logger.debug(f'checking for ort {orttype, ort} in db')
    date = datetime.now().strftime("%Y/%m/%d")
    corona_cursor.execute(f'SELECT * FROM CoronaData WHERE ort = {ort}, orttype = {orttype}, datum =  {date}')
    result = corona_cursor.fetchall()
    if result == []:
        return None
    else:
        return result[0]
    
    

def add_entry(ortdata):
    date = datetime.now().strftime("%Y/%m/%d")



if __name__ == '__main__':
    print(check_for_entry(None, None))
    

