import pytest
from glider import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    return app.test_client()

def test_3d_index_route(client):
    response = client.get('/3d')
    assert response.status_code == 200
    assert b'render3d.js' in response.data
    assert b'<canvas' not in response.data