from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os 

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)
Migrate(app, db)

# LOGIN CONFIG

login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login'



from halpreadsblog.error_pages.handlers import error_pages
from halpreadsblog.core.views import core
from halpreadsblog.users.views import users

app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(error_pages)
