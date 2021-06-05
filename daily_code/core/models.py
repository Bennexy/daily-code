import sys
import jwt
from datetime import datetime
from hashlib import md5
from os import abort
from time import time
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired
sys.path.append('.')

from app import config as app_config
from app import db
from daily_code.logger import get_logger

logger = get_logger("core-models")

user_cache = {}
user_cache_timeout = 15

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.string(127), primary_key=True)
    created_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))



    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_reset_password_token(self, expires_in=600):
        test = jwt.encode(
            {"reset_password": self.id, "exp": time() + expires_in},
            app_config.SECRET_KEY,
            algorithm="HS256",
        )
        return test

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, app_config.SECRET_KEY, algorithms=["HS256"])[
                "reset_password"
            ]
        except:
            return
        return User.query.get(id)

    def generate_auth_token(self, expiration=600):
        s = Serializer(app_config.SECRET_KEY, expires_in=expiration)
        return s.dumps({"id": self.id})


    @staticmethod
    def get_password_hash(password):
        return generate_password_hash(password)





