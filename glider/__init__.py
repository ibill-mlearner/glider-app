# glider/__init__.py

from flask import Flask

def create_app():
    app = Flask(__name__)

    # Future config or blueprint registration goes here
    from . import routes
    from .routes_3d import init_3d_routes
    from .routes_combined import init_combined_routes

    init_3d_routes(app)
    routes.init_app(app)
    init_combined_routes(app)

    return app