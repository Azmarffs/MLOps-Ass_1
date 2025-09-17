import numpy as np
from src.model.predict import make_prediction


class IdentityModel:
    def predict(self, X):
        return np.arange(len(X))


def test_make_prediction_list_of_dicts():
    model = IdentityModel()
    payload = [
        {"feature1": 0.1, "feature2": 0.2},
        {"feature1": 0.3, "feature2": 0.4},
    ]
    preds = make_prediction(model, payload)
    assert preds == [0, 1]


def test_make_prediction_dict_of_lists():
    model = IdentityModel()
    payload = {"feature1": [0.1, 0.2], "feature2": [0.3, 0.4]}
    preds = make_prediction(model, payload)
    assert preds == [0, 1]

