# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config  # Ensure this points to the right location

# Initialize Flask application
app = Flask(__name__)

# Load configuration from the Config class
app.config.from_object(Config)

# Initialize the SQLAlchemy database instance
db = SQLAlchemy(app)

# Import routes and models after the app is created
from app import routes, models
