# glider/__init__.py

from flask import Flask
from glider.routes_combined import init_combined_routes
from glider.resources import SimulationAPI
from glider.core.engine import GliderEngine
from glider.core.engine_3d import BlobEngine
from glider.core.glider_state_adapter import GliderStateAdapter
from glider.core.tick_controller import TickController
from glider import shapes

def create_app():
    app = Flask(__name__)

    # 2D engine setup
    engine = GliderEngine(100, 100)
    engine3d = BlobEngine(50)
    adapter = GliderStateAdapter(engine)
    tick_ctl = TickController(engine, interval=0.25)
    shape = shapes.toad()
    shapetd = shapes.shapeCube(12)
    engine3d.load_pattern(shapetd)
    engine.load_pattern(shape, offset_x=30, offset_y=10)

    # mount UI routes
    init_combined_routes(app)

    # mount API routes using class wrapper
    api = SimulationAPI(engine, adapter, tick_ctl, shape, prefix="api")
    app.register_blueprint(api.bp)

    return app