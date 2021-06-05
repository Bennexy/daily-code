from dotenv import find_dotenv, load_dotenv
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_env import MetaFlaskEnv

import app.config as app_config

import os


def load_configurations_file():
    ENV_FILE = find_dotenv()

    if ENV_FILE:
        load_dotenv(ENV_FILE)
        app_config.load_config()


def create_app_load_configurations():
    
    # load_configurations_file()
    app = Flask(__name__, static_folder="static", static_url_path="/static/")
    
    app.config.from_object("app.config")
    app.secret_key = app_config.SECRET_KEY
    app.application_name = app_config.APPLICATION_NAME
    
    return app


def init_login_manager(app):
    login = LoginManager(app)
    login.login_github_view = "github.login"
    login.login_view = "/login"
    return login


def init_db(app):
    db = SQLAlchemy(app)
    #db.create_engine(app.config["SQLALCHEMY_DATABASE_URI"], {})
    db.create_engine(app_config.SQLALCHEMY_DATABASE_URI, {})
    return db


def init_read_db(app):
    read_db = SQLAlchemy(app)
    read_db.create_engine(os.getenv("SQLALCHEMY_DATABASE_READ_AURI"), {})
    return read_db