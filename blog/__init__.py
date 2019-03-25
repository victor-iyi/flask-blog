from flask import Flask

from config import TEMPLATE_FOLDER, STATIC_FOLDER

app = Flask(__name__,
            static_folder=STATIC_FOLDER,
            template_folder=TEMPLATE_FOLDER)


from blog import routes
