# tests/test_routes_controls.py

import pytest
from glider import create_app
from glider.routes_combined import init_combined_routes


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    init_combined_routes(app)
    return app.test_client()


def test_start_stop_cycle(client):
    # start simulation
    resp = client.post("/api/start")
    assert resp.status_code == 200
    assert resp.get_json()["status"] == "running"

    # stop simulation
    resp = client.post("/api/stop")
    assert resp.status_code == 200
    assert resp.get_json()["status"] == "stopped"


def test_single_step(client):
    # perform a single step
    resp = client.post("/api/step")
    assert resp.status_code == 200
    data = resp.get_json()
    assert "gliders" in data and isinstance(data["gliders"], list)


def test_interval_change(client):
    resp = client.post("/api/interval", json={"interval": 0.1})
    assert resp.status_code == 200
    assert resp.get_json()["interval"] == 0.1