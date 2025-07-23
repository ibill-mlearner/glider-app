# glider/routes_combined.py

from flask import Blueprint, render_template


# ────────────────────────── blueprint ──
bp = Blueprint("combined", __name__, template_folder="templates")


# @bp.route("/2d")
# def index_combined():
#     """Serve the UI page that embeds controls + 2-D renderer."""
#     return render_template("2dplane.html")

@bp.route("/")
def index_combined():
    """Serve the UI page that embeds controls + 3-D renderer."""
    return render_template("3dplane.html")

def init_combined_routes(app):
    """Register this blueprint on a Flask app instance."""
    app.register_blueprint(bp)