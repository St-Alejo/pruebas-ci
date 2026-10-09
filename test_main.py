from fastapi.testclient import TestClient
from Lab08OctPruebas.main import app

client = TestClient(app)
def test_read_main():
    response = client.get("/")
    assert response.status_code == 20
    assert response.json() == {"status": "ok", "message": "API funcionando"}