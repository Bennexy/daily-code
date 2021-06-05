import os
import sys
sys.path.append('.')
from app import app
from daily_code.apps.corona import blueprint as corona




app.regster_blueprint(corona)