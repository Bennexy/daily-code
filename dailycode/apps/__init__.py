import os
import sys
sys.path.append('.')
from app import app
from app.apps.corona import blueprint as corona




app.regster_blueprint(corona)