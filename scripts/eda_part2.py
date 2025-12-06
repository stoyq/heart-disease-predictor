# eda_part2.py
# data: 2025-12-04

import os
import click
import pandas as pd

@click.command()
@click.option('--processed-training-data', type=str, help="Path to processed training data")
@click.option('--output-to', type=str, help="Path to directory where CSV will be saved")

def main(processed_training_data, output_to):
    '''Generates descriptive statistics and saves as CSV.'''

    data_clean = pd.read_csv(processed_training_data)
    df = data_clean.copy()

    # Generate descriptive statistics
    stats1 = df.describe()
    stats2 = df.nunique()

    info_data = []
    for col in df.columns:
        info_data.append({
            'Column': col,
            'Type': str(df[col].dtype),
            'Non-Null Count': df[col].notna().sum(),
            'Null Count': df[col].isna().sum()
        })
    info_df = pd.DataFrame(info_data)
    stats3 = info_df

    # Save as CSV
    if output_to:
        os.makedirs(output_to, exist_ok=True)
        stats_path = os.path.join(output_to, "describe_stats.csv")
        stats1.to_csv(stats_path)
        print(f"Saved: {stats_path}")
    if output_to:
        os.makedirs(output_to, exist_ok=True)
        stats_path = os.path.join(output_to, "unique_stats.csv")
        stats2.to_csv(stats_path)
        print(f"Saved: {stats_path}")
    if output_to:
        os.makedirs(output_to, exist_ok=True)
        stats_path = os.path.join(output_to, "info_stats.csv")
        stats3.to_csv(stats_path)
        print(f"Saved: {stats_path}")   


if __name__ == '__main__':
    main()