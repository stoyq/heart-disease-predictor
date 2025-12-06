"""
Script 04: Modeling and generating analysis outputs.

This script:
1. Reads the cleaned dataset from script 02.
2. Performs modeling.
3. Saves at least:
   - one figure
   - one summary table
to the output folder.

Usage:
    python scripts/04_model.py --input data/processed/cleveland_clean.csv \
                               --output results/analysis

Arguments:
    --input      Path to input cleaned CSV file.
    --output     Output file prefix (folder + filename prefix).
"""

import argparse
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report


def parse_args():
    parser = argparse.ArgumentParser(description="Modeling script for Milestone 3")
    parser.add_argument("--input", type=str, required=True,
                        help="Path to cleaned CSV file")
    parser.add_argument("--output", type=str, required=True,
                        help="Output file prefix (folder + prefix)")
    return parser.parse_args()


def main():
    args = parse_args()

    # Step 1. Load and clean data
    df = pd.read_csv(args.input)

    # Replace '?' with NaN and drop rows containing them
    df = df.replace('?', pd.NA)

    # Convert all columns to numeric where possible
    df = df.apply(pd.to_numeric, errors='ignore')

    # Drop rows with missing values (after '?' conversion)
    df = df.dropna()

    # Step 2. Simple train/test split
    X = df.drop(columns=["target"])
    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=2024, stratify=y
    )

    # Step 3. Fit a simple logistic regression model
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # Step 4. Predict on test
    y_pred = model.predict(X_test)

    # Step 5. Save classification report as a text table
    report = classification_report(y_test, y_pred, output_dict=True)
    report_df = pd.DataFrame(report)
    report_df.to_csv(f"{args.output}_classification_report.csv")

    # Step 6. Save a simple figure — model coefficients
    plt.figure(figsize=(10, 6))
    plt.bar(X.columns, model.coef_[0])
    plt.xticks(rotation=45, ha="right")
    plt.title("Logistic Regression Coefficients")
    plt.tight_layout()
    plt.savefig(f"{args.output}_coefficients.png")
    plt.close()

    print("Modeling completed successfully!")
    print(f"Saved: {args.output}_classification_report.csv")
    print(f"Saved: {args.output}_coefficients.png")


if __name__ == "__main__":
    main()
