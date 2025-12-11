# test_model_function

import pandas as pd
from src.modeling_functions import split_data, train_svc_model, evaluate_model


def test_split_data():
    df = pd.DataFrame({
        "feat1": [1,2,3,4,5],
        "feat2": [5,4,3,2,1],
        "target": [0,1,0,1,0]
    })

    X = df.drop(columns=["target"])
    y = df["target"]

    X_train, X_test, y_train, y_test = split_data(X, y)

    assert len(X_train) > 0
    assert len(X_test) > 0
    assert len(y_train) > 0
    assert len(y_test) > 0


def test_train_svc_model():
    df = pd.DataFrame({
        "feat1": [1,2,3,4],
        "feat2": [4,3,2,1],
        "target": [0,1,0,1]
    })

    X = df.drop(columns=["target"])
    y = df["target"]

    X_train, X_test, y_train, y_test = split_data(X, y)
    model = train_svc_model(X_train, y_train)

    assert hasattr(model, "predict")


def test_evaluate_model():
    df = pd.DataFrame({
        "feat1": [1,2,3,4],
        "feat2": [4,3,2,1],
        "target": [0,1,0,1]
    })

    X = df.drop(columns=["target"])
    y = df["target"]

    X_train, X_test, y_train, y_test = split_data(X, y)
    model = train_svc_model(X_train, y_train)
    report, cm = evaluate_model(model, X_test, y_test)

    assert isinstance(report, dict)
    assert cm.shape[0] == cm.shape[1]
