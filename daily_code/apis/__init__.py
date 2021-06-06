import sys
sys.path.append('.')

from daily_code import app

from daily_code.apis.corona import blueprint as corona
from daily_code.apis.db import blueprint as db


app.register_blueprint(corona)
app.register_blueprint(db)


