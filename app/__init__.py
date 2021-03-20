import os
from flask import Flask
from app.settings import Config, BASE_DIR
from flask_sqlalchemy import SQLAlchemy


template_dir = os.path.join(BASE_DIR, 'view/templates')
app = Flask(__name__, template_folder=template_dir)
app.config.from_object(Config)
db = SQLAlchemy(app)

from app.controller import ingrediente