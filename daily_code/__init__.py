
import os
import sys
import warnings
from flask_login import LoginManager, login_manager
from flask_migrate import Migrate
from flask_mail import Mail
from flask_httpauth import HTTPBasicAuth
from werkzeug.contrib.fixers import ProxyFix

sys.path.append('.')
warnings.filterwarnings('ignore')


from daily_code.app_initializer import *


app = create_app_load_configurations()
app.wsgi_app = ProxyFix(app.wsgi_app)



# setup mail
mail = Mail(app)


import daily_code.apis
import daily_code.apps
import daily_code.routes


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)







