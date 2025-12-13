import click
import os
import sys
import requests
import zipfile
import pandas as pd
from io import BytesIO
from pathlib import Path

sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from src.download_utility import url_is_working
from src.download_utility import file_exists

#import warnings
#warnings.filterwarnings("ignore")

# example usage from command line:
# python data_download.py --dataset_url="https://archive.ics.uci.edu/static/public/45/heart+disease.zip" --dataset_filename="processed.cleveland.data" --download_dir="../data/raw" --output_dir="../data/processed"

@click.command()
@click.option('--dataset_url', required=True, help='URL to data zip archive')
@click.option('--dataset_filename', required=True, help='Name of file within the zip archive')
@click.option('--download_dir', required=True, help='Path to download directory')
@click.option('--output_dir', required=True, help='Path to output directory')
@click.option('--debug', is_flag=True, default=False, help='Enable debug mode')
def main(dataset_url, dataset_filename, download_dir, output_dir, debug):
    # Debug input args
    if(debug):
        print('dataset_url:', dataset_url)
        print('dataset_filename:', dataset_filename)
        print('download_dir:', download_dir)
        print('output_dir:', output_dir)

    # This is the URL to the data. There are many files in the zip file
    # In particular we will retrieve the cleveland data
    url = dataset_url

    # Make sure the proper data folders exist
    os.makedirs(download_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)

    # Check URL validity
    if not url_is_working(url):
        print('Invalid URL')

    # Download the zip file into memory
    response = requests.get(url)

    try:
        # Open the zip from memory
        with zipfile.ZipFile(BytesIO(response.content)) as z:
            # We only want the Cleveland data
            z.extract(dataset_filename, download_dir)
            downloaded_path = download_dir + "/" + dataset_filename
    except zipfile.BadZipFile:
        print("Warning: Download not successful. Temporarily loading from local folder.")
        downloaded_path = download_dir + "/" + dataset_filename

    print(f"{'Raw data saved to:':<30}" + downloaded_path)

    cols = [
        "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
        "thalach", "exang", "oldpeak", "slope", "ca", "thal", "target"
    ]

    df = pd.read_csv(downloaded_path, header=None, names=cols)
    if(debug):
        print(df)

    # Write out processed data
    output_path = output_dir + "/cleveland_clean.csv"
    df.to_csv(output_path, index=False)
    print(f"{'Processed data saved to:':<30}" + output_path)

    # Check output file exists
    PROJECT_ROOT = Path(__file__).resolve().parent.parent
    output_file_path = PROJECT_ROOT / "data" / "processed" / "cleveland_clean.csv"
    if not file_exists(str(output_file_path)):
        print(f"Failed to write to: {output_file_path}")


if __name__ == '__main__':
    main()