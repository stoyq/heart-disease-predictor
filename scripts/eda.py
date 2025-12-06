# eda.py
# data: 2025-12-04

import os
import click
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['font.sans-serif'] = 'DejaVu Sans'
import matplotlib.pyplot as plt
import pandas as pd

@click.command()
@click.option('--processed-training-data', type=str, help="Path to processed training data")
@click.option('--plot-to', type=str, help="Path to directory where the plot will be written to")

def main(processed_training_data, plot_to):
    '''Plots the distribution of each feature from the processed data and also creates tables for EDA
       Also saves the plots and the tables.'''

    data_clean = pd.read_csv(processed_training_data)
    df = data_clean.copy()

    features = ["age", "chol", "trestbps", "thalach", "oldpeak", "sex"]

    # Create a 2x3 grid of subplots
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    axes = axes.flatten()

    for idx, feature in enumerate(features):
        ax = axes[idx]
        ax.hist(df[df['target'] == 0][feature], bins=20, alpha=0.6, label="No Disease")
        ax.hist(df[df['target'] == 1][feature], bins=20, alpha=0.6, label="Disease")
        ax.set_title(f"Distribution of {feature}")
        ax.set_xlabel(feature)
        ax.set_ylabel("Count")
        ax.legend()

    fig.subplots_adjust(hspace=0.4, wspace=0.3)
    
    # Save the grid plot
    if plot_to:
        os.makedirs(plot_to, exist_ok=True)
        plot_path = os.path.join(plot_to, "feature_distributions_grid.png")
        try:
            fig.savefig(plot_path, dpi=100, format='png')
            print(f"Saved: {plot_path}")
        except Exception as e:
            print(f"Error saving plot: {e}")
    
    plt.close(fig)


if __name__ == '__main__':
    main()