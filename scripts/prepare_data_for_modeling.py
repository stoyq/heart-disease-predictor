import click 
import os
import pandas as pd 
import pandera as pa
from deepchecks.tabular.checks import FeatureLabelCorrelation
from deepchecks.tabular.checks import FeatureFeatureCorrelation
from deepchecks.tabular import Dataset
from sklearn.model_selection import train_test_split


import sys 
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),".."))

from src.preapare_data_for_modeling_function import split_data


def create_dir_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

@click.command()
@click.option('--input_dir', required=True, help='Path (including filename) to raw data')
@click.option('--out_dir', required=True, help='Path to directory where the results should be saved')
def main(input_dir, out_dir):
    create_dir_if_not_exists(out_dir)

    # Load the data 
    cleveland_data = pd.read_csv(input_dir)

    # Remove rows with '?' in ca or thal
    cleveland_data = cleveland_data[~cleveland_data["ca"].astype(str).str.contains(r"\?")]
    cleveland_data = cleveland_data[~cleveland_data["thal"].astype(str).str.contains(r"\?")]

    #Data Validation

    schema = pa.DataFrameSchema( #Check Correct Colum Names, and Data Types
        {
            "age": pa.Column(int, pa.Check.between(18, 100),nullable=True,coerce=True), #No Outliers -> Check.between
            "sex": pa.Column(int, pa.Check.isin([0, 1]),nullable=True,coerce=True),  #Correct category levels -> Check.isin
            "cp": pa.Column(int, pa.Check.isin([1, 2, 3, 4]),nullable=True,coerce=True), #Missingness OK -> nullable= True 
            "trestbps": pa.Column(int,nullable=True,coerce=True),
            "chol": pa.Column(int,nullable=True,coerce=True),
            "fbs": pa.Column(int, pa.Check.isin([0, 1]),nullable=True,coerce=True),
            "restecg":  pa.Column(int, pa.Check.isin([0, 1, 2]), nullable=True,coerce=True),
            "thalach": pa.Column(int,nullable=True,coerce=True),
            "exang": pa.Column(int, pa.Check.isin([0, 1]),nullable=True,coerce=True),
            "oldpeak": pa.Column(float,nullable=True, coerce=True),
            "slope": pa.Column(int, pa.Check.isin([1, 2, 3]),nullable=True,coerce=True),
            "ca": pa.Column(float, pa.Check.isin([0, 1, 2, 3]),nullable=True,coerce=True),
            "thal": pa.Column(float,nullable=True, coerce=True),
            "target": pa.Column(int, pa.Check.isin([0, 1, 2, 3, 4]),nullable=True,coerce=True) #Target/response variable follows expected distribution
        },
        checks=[
            pa.Check(lambda df: ~df.duplicated().any(), error="Duplicate rows found."),  # No Duplicate Observations
            pa.Check(lambda df: ~(df.isna().all(axis=1)).any(), error="Empty rows found.") # No empty observations

        ]
    )

    cleveland_data = schema.validate(cleveland_data)#Validated Correct file format

    heart_train_ds = Dataset(cleveland_data, label="target", cat_features=["sex", "cp", "fbs", "restecg", "exang", "slope", "ca", "thal"])

    #Target-Feature Correlation Check - No anomalous target–feature correlations
    check_feat_lab_corr = FeatureLabelCorrelation().add_condition_feature_pps_less_than(0.6)
    check_feat_lab_corr_result = check_feat_lab_corr.run(dataset=heart_train_ds)

    if not check_feat_lab_corr_result.passed_conditions():
        raise ValueError("Feature-Label correlation exceeds the maximum acceptable threshold.")

    #Feature-Feature Correlation Check - No anomalous feature–feature correlations
    check_feat_feat_corr = FeatureFeatureCorrelation().add_condition_max_number_of_pairs_above_threshold(0.6)
    check_feat_feat_corr_result = check_feat_feat_corr.run(dataset=heart_train_ds)

    if not check_feat_feat_corr_result.passed_conditions():
        raise ValueError("Feature-Feature correlation exceeds the maximum acceptable threshold.")
    
    #Data Splitting 
    X = cleveland_data.drop(columns=["target"])
    y = cleveland_data["target"]

    X_train, X_test, y_train, y_test = split_data(X,y)
    
    # Merge target back before saving

    train_df = X_train.copy()
    train_df["target"] = y_train

    test_df = X_test.copy()
    test_df["target"] = y_test

    # Export X_train.csv and X_test.csv
    train_df.to_csv(os.path.join(out_dir, "X_train.csv"), index=False)
    test_df.to_csv(os.path.join(out_dir, "X_test.csv"), index=False)

    #Command to run script 
    #python scripts/prepare_data_for_modeling.py --input_dir data/processed/cleveland_clean.csv --out_dir data/processed

if __name__ == '__main__':
    main()