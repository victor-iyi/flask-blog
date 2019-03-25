from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import TEMPLATE_FOLDER, STATIC_FOLDER

# Flask app initialization.
app = Flask(__name__,
            static_folder=STATIC_FOLDER,
            template_folder=TEMPLATE_FOLDER)

# App configuration.
app.config['SECRET_KEY'] = '79dd045cc7abe191793a14ad54c7677f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Database handler.
db = SQLAlchemy(app)

# noqa: E402
from blog import routes
