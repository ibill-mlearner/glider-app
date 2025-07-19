# glider/routes_combined.py

from flask import Blueprint, jsonify, render_template, request
from glider.core.engine import GliderEngine
from glider.core.tick_controller import TickController
from glider.core.glider_state_adapter import GliderStateAdapter
from glider import shapes
# ────────────────────────── engine + adapter ──
engine = GliderEngine(100, 100)
adapter = GliderStateAdapter(engine)

"""
Available Shape Patterns:
shape() – returns a 10x10 random grid of 0s and 1s. Useful for noise testing or chaos.
block() – 2x2 still life. Stable, does not evolve.
blinker() – 3x1 oscillator. Flips between vertical and horizontal every tick.
glider() – smallest moving spaceship. Moves diagonally across the grid.
glider_plus() – a glider with an attached vertical blinker. Complex hybrid motion.
beacon() – two adjacent 2x2 blocks offset diagonally. Period-2 oscillator.
toad() – 2-row, 4-cell oscillator. Period-2, shifts phase and shape.
pulsar() – large symmetric oscillator. Period-3 with complex concentric activity.
You can plug any of these into engine.load_pattern() via shape = shapes.name()
"""
shape = shapes.toad()

engine.load_pattern(shape, offset_x=30, offset_y=10)

# background tick controller (interval can be adjusted later)
tick_ctl = TickController(engine, interval=0.25)

# ────────────────────────── blueprint ──
bp = Blueprint("combined", __name__, template_folder="templates")


@bp.route("/")
def index_combined():
    """Serve the UI page that embeds controls + 3-D renderer."""
    return render_template("index_combined.html")


# live state
@bp.route("/api/state", methods=["GET"])
def api_state():
    return jsonify(adapter.to_json_payload())


# control endpoints
@bp.route("/api/start", methods=["POST"])
def api_start():
    tick_ctl.start()
    return jsonify({"status": "running"})


@bp.route("/api/stop", methods=["POST"])
def api_stop():
    tick_ctl.stop()
    return jsonify({"status": "stopped"})


@bp.route("/api/step", methods=["POST"])
def api_step():
    tick_ctl.step_once()
    return jsonify(adapter.to_json_payload())

@bp.route("/api/clear", methods=["PUT"])
def api_clear():
    print("[CLEAR] Glider reset triggered")
    tick_ctl.clear(shape)
    return jsonify({"status": "cleared"})

@bp.route("/api/tick", methods=["POST"])
def api_tick():
    tick_ctl.step_once()
    return jsonify(adapter.to_json_payload())

# optional: adjust tick interval on the fly
@bp.route("/api/interval", methods=["POST"])
def api_interval():
    try:
        new_interval = float(request.json.get("interval"))
        tick_ctl.set_interval(new_interval)
        return jsonify({"status": "ok", "interval": new_interval})
    except (TypeError, ValueError):
        return jsonify({"status": "error", "msg": "invalid interval"}), 400


def init_combined_routes(app):
    """Register this blueprint on a Flask app instance."""
    app.register_blueprint(bp)