from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt  
from flask_login import LoginManager

app_auth = Flask(__name__)

app_auth.config['SECRET_KEY'] = 'your_secret_key'
app_auth.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app_auth)
bcrypt = Bcrypt(app_auth)

login_manager = LoginManager(app_auth)
login_manager.login_view = 'login'

from app_auth import routes