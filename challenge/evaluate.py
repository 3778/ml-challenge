import pandas as pd
import numpy as np
import sklearn.metrics as sklearn_metrics


def evaluate_regression(y_pred):
    """Evaluates predictions with multiple metrics

    For details on metrics see
    https://scikit-learn.org/stable/modules/model_evaluation.html

    Args:
        y_pred (array): Predictions from regression model.

    Returns:
        dict: Evaluation results on multiple metrics.
    """
    y_true = pd.read_csv('data/answers.csv')
    metrics_to_evaluate = ['explained_variance_score',
                           'mean_absolute_error',
                           'mean_squared_error',
                           'mean_squared_log_error',
                           'median_absolute_error',
                           'r2_score']
    return {m: getattr(sklearn_metrics, m)(y_true, y_pred)
            for m in metrics_to_evaluate}
