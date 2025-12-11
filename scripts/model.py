"""
Script 04: Modeling and generating analysis outputs (SVC version).

This script:
1. Reads the cleaned dataset from script 02.
2. Trains an SVC classifier (consistent with proposal).
3. Saves:
   - classification report
   - confusion matrix plot
"""

import argparse
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, ConfusionMatrixDisplay


def parse_args():
    parser = argparse.ArgumentParser(description="Modeling script for Milestone 3 (SVC)")
    parser.add_argument("--input", type=str, required=True,
                        help="Path to cleaned CSV file")
    parser.add_argument("--output", type=str, required=True,
                        help="Output file prefix (folder + prefix)")
    return parser.parse_args()


def main():
    args = parse_args()

    # Step 1. Load data
    df = pd.read_csv(args.input)

    # Clean missing '?'
    df = df.replace('?', pd.NA)
    df = df.apply(pd.to_numeric, errors='ignore')
    df = df.dropna()

    # Step 2. Split
    X = df.drop(columns=["target"])
    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=2024, stratify=y
    )

    # Step 3. Train SVC
    model = SVC(kernel='rbf', C=1.0, gamma='scale')  # standard baseline SVC
    model.fit(X_train, y_train)

    # Step 4. Predictions
    y_pred = model.predict(X_test)

    # Step 5. Save classification report
    report = classification_report(y_test, y_pred, output_dict=True)
    report_df = pd.DataFrame(report)
    report_df.to_csv(f"{args.output}_classification_report.csv")

    # Step 6. Save confusion matrix
    disp = ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
    plt.title("Confusion Matrix - SVC")
    plt.tight_layout()
    plt.savefig(f"{args.output}_confusion_matrix.png")
    plt.close()

    print("Modeling with SVC completed successfully!")
    print(f"Saved: {args.output}_classification_report.csv")
    print(f"Saved: {args.output}_confusion_matrix.png")


if __name__ == "__main__":
    main()


