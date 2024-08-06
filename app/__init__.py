from flask import Flask
from .views.movie_views import movie_views
from .views.top20_views import top20_views
from dotenv import load_dotenv
import os

def create_app():
    # Load environment variables from .env file
    load_dotenv()

    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Register Blueprints
    app.register_blueprint(movie_views)
    app.register_blueprint(top20_views)

    return app
