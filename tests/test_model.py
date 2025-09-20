import numpy as np
from src.model.predict import make_prediction


class IdentityModel:
    def predict(self, X):
        return np.arange(len(X))


def test_make_prediction_list_of_dicts():
    model = IdentityModel()
    payload = [
        {"Pclass": 3, "Sex": "male", "Age": 22, "SibSp": 1, "Parch": 0, "Fare": 7.25, "Embarked": "S"},
        {"Pclass": 1, "Sex": "female", "Age": 38, "SibSp": 1, "Parch": 0, "Fare": 71.2833, "Embarked": "C"},
    ]
    preds = make_prediction(model, payload)
    assert preds == [0, 1]


def test_make_prediction_dict_of_lists():
    model = IdentityModel()
    payload = {
        "Pclass": [3, 1],
        "Sex": ["male", "female"],
        "Age": [22, 38],
        "SibSp": [1, 1],
        "Parch": [0, 0],
        "Fare": [7.25, 71.2833],
        "Embarked": ["S", "C"],
    }
    preds = make_prediction(model, payload)
    assert preds == [0, 1]

