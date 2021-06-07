import sys
import mysql.connector
from mysql.connector import cursor
sys.path.append('.')
from daily_code.config import *
from daily_code.logger import get_logger

logger = get_logger('db-actions')

mydb = mysql.connector.connect(
    host=DB,
    port=DB_PORT,
    user=DB_USER,
    password=DB_PASSWORD
)