# test_SVC_Modeling_function.py

import pandas as pd
from src.SVC_Modeling_functions import split_data, train_svc_model, evaluate_model


def test_split_data():
    """Test that split_data returns non-empty splits."""
    df = pd.DataFrame({
        "feat1": [1, 2, 3, 4, 5],
        "feat2": [5, 4, 3, 2, 1],
        "target": [0, 1, 0, 1, 0]
    })

    X = df.drop(columns=["target"])
    y = df["target"]

    X_train, X_test, y_train, y_test = split_data(X, y)

    assert len(X_train) > 0
    assert len(X_test) > 0
    assert len(y_train) > 0
    assert len(y_test) > 0


def test_train_svc_model():
    """Test that train_svc_model returns a trained model with predict()."""
    df = pd.DataFrame({
        "feat1": [1, 2, 3, 4],
        "feat2": [4, 3, 2, 1],
        "target": [0, 1, 0, 1]
    })

    X = df.drop(columns=["target"])
    y = df["target"]

    X_train, X_test, y_train, y_test = split_data(X, y)
    model = train_svc_model(X_train, y_train)

    assert hasattr(model, "predict"), "Model must implement predict()."


def test_evaluate_model():
    """Test evaluate_model returns a DataFrame and square confusion matrix."""
    df = pd.DataFrame({
        "feat1": [1, 2, 3, 4],
        "feat2": [4, 3, 2, 1],
        "target": [0, 1, 0, 1]
    })

    X = df.drop(columns=["target"])
    y = df["target"]

    X_train, X_test, y_train, y_test = split_data(X, y)
    model = train_svc_model(X_train, y_train)

    report_df, cm = evaluate_model(model, X_test, y_test)

    # report_df a pandas DataFrame 
    assert isinstance(report_df, pd.DataFrame), "report must be a pandas DataFrame"

    # confusion matrix must be a 2x2 square matrix for binary classification
    assert cm.shape[0] == cm.shape[1], "Confusion matrix must be square"
