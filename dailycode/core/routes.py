import sys
from flask import Blueprint
sys.path.append('.')


core = Blueprint('core', __name__)


@core.route("/")
def index():
    return("im the core page and im running!")

