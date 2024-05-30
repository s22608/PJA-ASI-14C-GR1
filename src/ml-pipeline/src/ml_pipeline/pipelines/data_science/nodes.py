import logging
from typing import Dict

import pandas as pd
from autogluon.tabular import TabularPredictor


def train_model(train_data: pd.DataFrame) -> TabularPredictor:
    label_column = 'target'
    predictor = TabularPredictor(label=label_column).fit(train_data)
    return predictor


def evaluate_model(predictor: TabularPredictor, test_data: pd.DataFrame) -> Dict[str, float]:
    y_test = test_data['target']
    test_data_nolab = test_data.drop(columns=['target'])

    predictions = predictor.predict(test_data_nolab)

    score = predictor.evaluate_predictions(y_true=y_test, y_pred=predictions, auxiliary_metrics=True)

    logger = logging.getLogger(__name__)
    logger.info("Model has been evaluated. Metrics: %s", score)
    return score
