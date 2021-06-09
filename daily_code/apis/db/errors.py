import sys
sys.path.append('.')
from daily_code.logger import get_logger

logger = get_logger('db-api-errors')

class DBAPIErrpr(Exception):
    def __init__(self, message, error):
        logger.error(f"an error {error}, with the messge {message} occured")

class UnknownDataType(DBAPIErrpr):
    def __init__(self, message):
        super().__init__(message, UnknownDataType)
