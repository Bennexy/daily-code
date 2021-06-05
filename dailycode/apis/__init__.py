import sys
sys.path.append('.')

from app import app

from app.apis.corona import blueprint as corona


app.register_blueprint(corona)


