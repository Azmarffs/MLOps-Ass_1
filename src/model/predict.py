from typing import Any, Dict, List, Union
import numpy as np
import pandas as pd


REQUIRED_COLUMNS = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']


def _to_dataframe(payload: Union[Dict[str, List], List[Dict]]) -> pd.DataFrame:
    if isinstance(payload, dict):
        df = pd.DataFrame(payload)
    elif isinstance(payload, list):
        df = pd.DataFrame(payload)
    else:
        raise ValueError('Unsupported payload format')
    return df


def _ensure_columns(df: pd.DataFrame) -> pd.DataFrame:
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required input fields: {missing}")
    return df[REQUIRED_COLUMNS]


def make_prediction(model: Any, payload: Union[Dict[str, List], List[Dict]]):
    df = _to_dataframe(payload)
    df = _ensure_columns(df)
    preds = model.predict(df)
    if isinstance(preds, np.ndarray):
        return preds.tolist()
    return list(preds)

