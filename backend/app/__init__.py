from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)
CORS(app, supports_credentials=True)  # Enable CORS with support for credentials
app.config.from_object('config.Config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes  # Import routes after initializing the app
