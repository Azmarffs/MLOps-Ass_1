import pickle
from pathlib import Path
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LogisticRegression


TITANIC_FEATURES = [
    'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked'
]
TARGET_COLUMN = 'Survived'


def build_pipeline() -> Pipeline:
    numeric_features = ['Age', 'SibSp', 'Parch', 'Fare']
    categorical_features = ['Pclass', 'Sex', 'Embarked']

    numeric_transformer = SimpleImputer(strategy='median')
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore')),
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features),
        ]
    )

    clf = LogisticRegression(max_iter=1000)

    model = Pipeline(steps=[('preprocess', preprocessor), ('model', clf)])
    return model


def train_and_save_model(dataset_path: str = 'src/data/dataset.csv', model_out: str = 'src/model/model.pkl') -> None:
    df = pd.read_csv(dataset_path)
    missing_cols = [c for c in TITANIC_FEATURES if c not in df.columns]
    if missing_cols:
        raise ValueError(f"Dataset missing required columns: {missing_cols}")

    X = df[TITANIC_FEATURES]
    y = df[TARGET_COLUMN]

    model = build_pipeline()
    model.fit(X, y)

    Path(model_out).parent.mkdir(parents=True, exist_ok=True)
    with open(model_out, 'wb') as f:
        pickle.dump(model, f)


if __name__ == '__main__':
    train_and_save_model()

