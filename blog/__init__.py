from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import TEMPLATE_FOLDER, STATIC_FOLDER

app = Flask(__name__,
            static_folder=STATIC_FOLDER,
            template_folder=TEMPLATE_FOLDER)
db = SQLAlchemy(app)

# noqa: E402
from blog import routes
