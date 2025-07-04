import pytest
from glider import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    return app.test_client()

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'<canvas' in response.data

def test_api_state_route(client):
    response = client.get('/api/state')
    assert response.status_code == 200
    data = response.get_json()
    assert 'gliders' in data