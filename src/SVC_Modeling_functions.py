"""
Utility functions for SVC modeling used in Milestone 3 & 4.

Includes:
- split_data: safely split data with fallback for tiny datasets
- train_svc_model: trains a linear SVC classifier
- evaluate_model: returns classification report + confusion matrix
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix


def split_data(X, y, test_size=0.2, random_state=522):
    """
    Splits data into train and test sets.
    Uses stratification when possible.
    Falls back to non-stratified split for very small datasets.

    This prevents sklearn ValueError in unit tests.
    """
    try:
        return train_test_split(
            X, y,
            test_size=test_size,
            random_state=random_state,
            stratify=y
        )
    except ValueError:
        # Fallback: no stratification (needed for tiny test datasets)
        return train_test_split(
            X, y,
            test_size=test_size,
            random_state=random_state,
            stratify=None
        )


def train_svc_model(X_train, y_train):
    """Trains a linear SVC classifier and returns the model."""
    model = SVC(kernel="linear")
    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test, y_test):
    """
    Evaluates the SVC model.

    Returns:
        report_df (DataFrame): classification report
        cm (ndarray): confusion matrix
    """
    y_pred = model.predict(X_test)

    report_dict = classification_report(y_test, y_pred, output_dict=True)
    report_df = pd.DataFrame(report_dict)

    cm = confusion_matrix(y_test, y_pred)

    return report_df, cm
