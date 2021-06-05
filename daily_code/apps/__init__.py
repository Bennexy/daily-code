import os
import sys
sys.path.append('.')
from daily_code import app
from daily_code.apps.corona import blueprint as corona




app.register_blueprint(corona)