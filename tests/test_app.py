import json
from src.app import app


class DummyModel:
    def predict(self, X):
        return [0 for _ in range(len(X))]


def test_health():
    client = app.test_client()
    resp = client.get('/health')
    assert resp.status_code == 200
    assert resp.get_json()['status'] in {'healthy', 'model_missing'}


def test_predict(monkeypatch):
    # monkeypatch the global model in app
    import src.app as app_module
    app_module.model = DummyModel()
    client = app.test_client()
    payload = {'feature1': [0.1, 0.2], 'feature2': [0.3, 0.4]}
    resp = client.post('/predict', data=json.dumps(payload), content_type='application/json')
    assert resp.status_code == 200
    data = resp.get_json()
    assert 'prediction' in data
    assert data['prediction'] == [0, 0]

