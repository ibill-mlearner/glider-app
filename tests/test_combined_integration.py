# tests/test_combined_integration.py

import pytest
from glider import create_app
from glider.routes_combined import init_combined_routes


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    # register combined blueprint
    init_combined_routes(app)
    return app.test_client()


def test_combined_page_loads(client):
    """GET /combined returns HTML and status 200."""
    resp = client.get("/combined")
    assert resp.status_code == 200
    assert b"<canvas" in resp.data or b"render3d.js" in resp.data


def test_api_state_returns_cells(client):
    """GET /api/state returns expected JSON structure."""
    resp = client.get("/api/state")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["status"] == "ok"
    assert "gliders" in data and isinstance(data["gliders"], list)
    # At least one glider block seeded in blueprint setup
    cells = data["gliders"][0]["cells"]
    assert any(isinstance(c, list) and len(c) == 2 for c in cells)