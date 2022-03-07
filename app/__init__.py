from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import create_db
import os
persistent_path = os.getenv("PERSISTENT_STORAGE_DIR")

create_db.create_connection("sqlite.db", persistent_path)

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///{persistent_path}\sqlite.db'
app.config["SQLALCHEMY_ECHO"] = False
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

from app import views
from app import models

db.init_app(app)
db.create_all() 