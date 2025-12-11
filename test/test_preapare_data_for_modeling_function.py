import sys 
import os 
import pandas as pd

sys.path.append(os.path.join(os.path.dirname(__file__),".."))

from src.preapare_data_for_modeling_function import split_data

data = {
    "age":      [63.0, 67.0, 67.0, 37.0, 41.0, 56.0, 62.0, 57.0, 63.0, 53.0],
    "sex":      [1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0],
    "cp":       [1.0, 4.0, 4.0, 3.0, 2.0, 2.0, 4.0, 4.0, 4.0, 4.0],
    "trestbps": [145.0, 160.0, 120.0, 130.0, 130.0, 120.0, 140.0, 120.0, 130.0, 140.0],
    "chol":     [233.0, 286.0, 229.0, 250.0, 204.0, 236.0, 268.0, 354.0, 254.0, 203.0],
    "fbs":      [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0],
    "restecg":  [2.0, 2.0, 2.0, 0.0, 2.0, 0.0, 2.0, 0.0, 2.0, 2.0],
    "thalach":  [150.0, 108.0, 129.0, 187.0, 172.0, 178.0, 160.0, 163.0, 147.0, 155.0],
    "exang":    [0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0],
    "oldpeak":  [2.3, 1.5, 2.6, 3.5, 1.4, 0.8, 3.6, 0.6, 1.4, 3.1],
    "slope":    [3.0, 2.0, 2.0, 3.0, 1.0, 1.0, 3.0, 1.0, 2.0, 3.0],
    "ca":       [0.0, 3.0, 2.0, 0.0, 0.0, 0.0, 2.0, 0.0, 1.0, 0.0],
    "thal":     [6.0, 3.0, 7.0, 3.0, 3.0, 3.0, 3.0, 3.0, 7.0, 7.0],
    "target":   [0, 2, 1, 0, 0, 0, 3, 0, 2, 1]
}

df = pd.DataFrame(data)

X = df.drop(columns=["target"])
y = df["target"] 

def test_split_data_types():
    X_train, X_test, y_train, y_test  = split_data(X,y)

    assert isinstance(X_train, pd.DataFrame)
    assert isinstance(X_test, pd.DataFrame)
    assert isinstance(y_train, pd.Series)
    assert isinstance(y_test, pd.Series)

def test_split_data_dimensions():
    X_train, X_test, y_train, y_test  = split_data(X,y)

    assert X_train.shape[0] ==  y_train.shape[0]
    assert X_test.shape[0] ==  y_test.shape[0]
