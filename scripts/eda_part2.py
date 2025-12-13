# eda_part2.py
# data: 2025-12-04

import os
import click
import pandas as pd
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.describe_data import describe_data


@click.command()
@click.option('--processed-training-data', type=str, help="Path to processed training data")
@click.option('--output-to', type=str, help="Path to directory where CSV will be saved")

def main(processed_training_data, output_to):
    '''Generates descriptive statistics and saves as CSV.'''

    data_clean = pd.read_csv(processed_training_data)
    df = data_clean.copy()
    stats = describe_data(df)

    # Save as CSV
    if output_to:
        os.makedirs(output_to, exist_ok=True)
        stats_path = os.path.join(output_to, "describe_stats.csv")
        stats[0].to_csv(stats_path)
        print(f"Saved: {stats_path}")
    if output_to:
        os.makedirs(output_to, exist_ok=True)
        stats_path = os.path.join(output_to, "unique_stats.csv")
        stats[1].to_csv(stats_path)
        print(f"Saved: {stats_path}")
    if output_to:
        os.makedirs(output_to, exist_ok=True)
        stats_path = os.path.join(output_to, "info_stats.csv")
        stats[2].to_csv(stats_path)
        print(f"Saved: {stats_path}")   


if __name__ == '__main__':
    main()