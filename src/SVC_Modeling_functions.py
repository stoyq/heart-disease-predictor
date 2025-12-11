#Create a function file inside src/model.py

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd


def split_data(X, y, test_size=0.2, random_state=522):
    """Split data into train/test sets."""
    return train_test_split(X, y, test_size=test_size, random_state=random_state, stratify=y)


def train_svc_model(X_train, y_train):
    """Train SVC model."""
    model = SVC(kernel="linear", probability=False)
    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test, y_test):
    """Return classification report and confusion matrix."""
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred, output_dict=True)
    cm = confusion_matrix(y_test, y_pred)
    return report, cm
