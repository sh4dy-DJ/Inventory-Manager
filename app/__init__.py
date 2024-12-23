from flask import Flask
from .routes import main  # Import the main blueprint
import os

def create_app():
    # Define the static folder explicitly
    app = Flask(__name__, static_folder=os.path.join(os.getcwd(), 'static'))

    # Register the blueprint
    app.register_blueprint(main, url_prefix='/')

    return app
