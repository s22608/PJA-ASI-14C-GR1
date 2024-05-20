import logging
from typing import Dict, Tuple

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import r2_score, mean_absolute_error, max_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


def split_data(data: pd.DataFrame, parameters: Dict) -> Tuple:
    imputer = SimpleImputer(strategy='most_frequent')
    data_filled = pd.DataFrame(imputer.fit_transform(data), columns=data.columns)

    label_encoders = {}
    for column in data_filled.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        data_filled[column] = le.fit_transform(data_filled[column])
        label_encoders[column] = le

    X = data_filled.drop('target', axis=1)
    y = data_filled['target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test


def train_model(X_train: pd.DataFrame, y_train: pd.Series) -> RandomForestClassifier:
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model


def evaluate_model(
    model: RandomForestClassifier, X_test: pd.DataFrame, y_test: pd.Series
):
    y_pred = model.predict(X_test)
    score = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    me = max_error(y_test, y_pred)
    logger = logging.getLogger(__name__)
    logger.info("Model has a coefficient R^2 of %.3f on test data.", score)
    return {"r2_score": score, "mae": mae, "max_error": me}

