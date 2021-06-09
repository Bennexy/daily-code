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
    date = datetime.now().strftime("%Y-%m-%d")
    corona_cursor.execute(f'SELECT * FROM CoronaData WHERE ortsnamen = "{ort}" AND orttype = "{orttype}" AND datum =  "{date}"')
    result = corona_cursor.fetchall()
    #logger.debug(result)
    if result == []:
        return None
    else:
        return result[0]
    
    

def add_entry(data):
    logger.debug(f'adding ortdata to db {data}')
    date = datetime.now().strftime("%Y-%m-%d")
    orttype = data['orttype']
    ort = data['ortsnamen']
    if check_for_entry(ort, orttype) == None:
        einwohner = float(data['einwohner'])
        infektionen = float(data['infektionen'])
        infektionsrate = float(data['infektionsrate'].rstrip("%").replace(',', '.'))
        neuinfektionen = float(data['neuinfektionen'].replace(',', '.'))
        todesfälle = float(data['todesfaelle'])
        letalitaetsrate = float(data['letalitaetsrate'].rstrip("%").replace(',', '.'))
        if 'erstimpfungen' in data:
            erstimpfungen = float(data['erstimpfungen'])
            impfquote_erstimpfungen = float(data['impfquote-(erstimpfung)'].rstrip("%").replace(',', '.'))
            impfquote_vollständing = float(data['impfquote-(vollstaeding)'].rstrip("%").replace(',', '.'))
            corona_cursor.execute(f'INSERT INTO CoronaData (ortsnamen, orttype, einwohner, infektionen, infektionsrate, neuinfektionen, todesfaelle, letalitaetsrate, datum, erstimpfungen, impfquote_erstimpfung, impfquote_vollstaendig) VALUES ("{ort}", "{orttype}", "{einwohner}", "{infektionen}", "{infektionsrate}", "{neuinfektionen}", "{todesfälle}", "{letalitaetsrate}", "{date}", "{erstimpfungen}", "{impfquote_erstimpfungen}","{impfquote_vollständing}")')

        else:
            corona_cursor.execute(f'INSERT INTO CoronaData (ortsnamen, orttype, einwohner, infektionen, infektionsrate, neuinfektionen, todesfaelle, letalitaetsrate, datum) VALUES ("{ort}", "{orttype}", "{einwohner}", "{infektionen}", "{infektionsrate}", "{neuinfektionen}", "{todesfälle}", "{letalitaetsrate}", "{date}")')


        
        mydb.commit()
        logger.debug(f'added data to db')
        return f'data has been added to db'
    else:
        logger.debug(f'data has allready been added to db')
        return "data has allready been added to db"





