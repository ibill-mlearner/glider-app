# glider/routes_combined.py

from flask import Blueprint, jsonify, render_template, request
from glider.core.engine import GliderEngine
from glider.core.tick_controller import TickController
from glider.core.glider_state_adapter import GliderStateAdapter

# ────────────────────────── engine + adapter ──
engine = GliderEngine(50, 30)
adapter = GliderStateAdapter(engine)

# seed a simple block so scene isn’t empty
block = [
    [1, 1],
    [1, 1]
]
engine.load_pattern(block, offset_x=10, offset_y=10)

# background tick controller (interval can be adjusted later)
tick_ctl = TickController(engine, interval=0.25)

# ────────────────────────── blueprint ──
bp = Blueprint("combined", __name__, template_folder="templates")


@bp.route("/combined")
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