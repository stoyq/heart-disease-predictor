import click 
import os
import pandas as pd 
import pandera as pa
from deepchecks.tabular.checks import FeatureLabelCorrelation
from deepchecks.tabular.checks import FeatureFeatureCorrelation
from deepchecks.tabular import Dataset
from sklearn.model_selection import train_test_split

def create_dir_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

@click.command()
@click.option('--input_dir', required=True, help='Path (including filename) to raw data')
@click.option('--out_dir', required=True, help='Path to directory where the results should be saved')
def main(input_dir, out_dir):
    create_dir_if_not_exists(out_dir)


if __name__ == '__main__':
    main()