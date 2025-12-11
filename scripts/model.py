"""
SVC Modeling Script for Milestone 3
-----------------------------------

This script:
1. Loads the cleaned dataset.
2. Trains an SVC (Support Vector Classifier).
3. Saves:
   - model_confusion_matrix.png
   - model_classification_report.csv

Usage:
    python scripts/model.py --input data/processed/cleveland_clean.csv \
                            --output results/model
"""

import argparse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, classification_report

def parse_args():
    parser = argparse.ArgumentParser(description="SVC model for heart disease prediction")
    parser.add_argument("--input", required=True, help="Path to cleaned CSV file")
    parser.add_argument("--output", required=True, help="Output path prefix")
    return parser.parse_args()

def main():
    args = parse_args()

    # --------------------------
    # Step 1: Load and clean data
    # --------------------------
    df = pd.read_csv(args.input)
    df = df.replace("?", pd.NA)
    df = df.dropna()
    df = df.apply(pd.to_numeric, errors="ignore")

    X = df.drop(columns=["target"])
    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=2024, stratify=y
    )

    # --------------------------
    # Step 2: Train SVC model
    # --------------------------
    model = SVC(kernel="linear", probability=False)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # --------------------------
    # Step 3: Save classification report (CSV)
    # --------------------------
    report_dict = classification_report(y_test, y_pred, output_dict=True)
    report_df = pd.DataFrame(report_dict)
    csv_path = f"{args.output}_classification_report.csv"
    report_df.to_csv(csv_path, index=True)

    # --------------------------
    # Step 4: Save confusion matrix figure
    # --------------------------
    cm = confusion_matrix(y_test, y_pred)

    plt.imshow(cm, cmap="Blues")
plt.colorbar()
plt.title("SVC Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")

# Add cell labels manually
for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        plt.text(j, i, cm[i, j], ha="center", va="center", color="black")

plt.tight_layout()
plt.savefig(f"{args.output}_confusion_matrix.png")
plt.close()
