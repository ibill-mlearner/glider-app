# glider/__init__.py

from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes_combined import init_combined_routes

    init_combined_routes(app)

    return app