import sys
sys.path.append('.')
from flask import Blueprint, url_for
from flask_restx import Api


blueprint = Blueprint(
    "db_api", __name__, url_prefix="/api/db"
)


# init myapi as a subclass from api
class MyApi(Api):
    @property
    def specs_url(self):
        """Monkey patch for HTTPS"""
        scheme = "http" if "5000" in self.base_url else "https"
        return url_for(self.endpoint("specs"), _external=True, _scheme=scheme)

api = MyApi(
    blueprint,
    version="1.0.1",
    title="Daily-Code - db api",
    contact="benedikt.liebs@daily-code.de",
    description="Corona api",
)

from daily_code.apis.db.namespaces.endpoints import namespace as namespace_db


api.add_namespace(namespace_db, path='/db')