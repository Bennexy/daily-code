import sys
from flask_sitemap import Sitemap
from flask import render_template
sys.path.append('.')
from app import app
from daily_code.core.routes import core

app.register_blueprint(core)


@app.errorhandler(404)
def not_found_error(error):
    return "this site does not exsist", 404
    # return render_template("public/404.html"), 404

from daily_code.core.routes import core
app.register_blueprint(core)





ext = Sitemap(app=app)


@ext.register_generator
def index():
    # Not needed if you set SITEMAP_INCLUDE_RULES_WITHOUT_PARAMS=True
    yield "index", {}


@ext.register_generator
def corona():
    yield "corona", {}


