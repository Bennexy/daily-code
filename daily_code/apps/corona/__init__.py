import sys
sys.path.append(".")

from daily_code.logger import get_logger
from flask import Blueprint, render_template, request



blueprint = Blueprint(
    "corona_app_bp", __name__, url_prefix="/apps/corona", template_folder="templates"
)

api_endpoint = "/api/corona/"

logger = get_logger("blueprint_corona_app")


@blueprint.route("/")
def index():
    return "Welcome to the corona app"








