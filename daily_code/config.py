from os import getenv as env
from dotenv import find_dotenv, load_dotenv

ENV_FILE = find_dotenv()

if ENV_FILE:
    load_dotenv(ENV_FILE)


SECRET_KEY = env("SECRET_KEY")
SQLALCHEMY_DATABASE_URI = env('SQLALCHEMY_DATABASE_URI')
APPLICATION_NAME = env('APPLICATION_NAME')
CoronaServerUrl = env("CoronaServerUrl")

