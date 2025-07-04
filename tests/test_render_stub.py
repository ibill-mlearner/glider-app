import pytest
from glider import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    return app.test_client()

def test_js_renderer_included(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'render.js' in response.data
    assert b'<canvas id="glider-canvas">' in response.data