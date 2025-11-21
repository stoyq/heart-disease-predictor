# Heart Disease Predictor

- Authors: Johnson Chuang | Eduardo Sanches | Azadeh Ramesh | Jose Davila

Data analysis and workflow project for DSCI 522 (Data Science Workflows), a course in the Master of Data Science program at the University of British Columbia.

## Summary

In this project, we use the UCI Heart Disease dataset to build a machine-learning model that predicts whether a patient is likely to have heart disease based on clinical and physiological attributes. Our results highlight key risk indicators that align with well-known medical knowledge, demonstrating how machine learning can support early screening and clinical decision-making.

## About the Dataset

The data set that was used in this project can be found [here](https://archive.ics.uci.edu/dataset/45/heart+disease). It contains 303 observations, 14 features and a target value used to indicate the diagnosis of heart disease.


## Report

The final report can be found [here](doc/heart_disease_project_doc.pdf).

## Dependencies

This project uses the following libraries and modules. We recommend using conda to reproduce the same environment. See Usage section below for installation notes.

  - python>=3.11
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - scikit-learn
  - requests
  - jupyterlab
  - ucimlrepo
  - conda-lock
  - pip

## Usage

Follow the instructions below to reproduce the analysis.

#### Setup

1. Clone this GitHub repository.

```
git clone git@github.com:stoyq/heart-disease-predictor.git
```

2. Setup the conda environment by running

```
conda env create --file environment.yml
```

Alternatively, we have also provided a conda-lock file. Please refer to the [conda-lock documentation](https://github.com/conda/conda-lock) for basic usage.

3. Once the environment has been created, activate the environment

```
conda activate group25-env
```

4. Run Jupyter Lab

```
jupyter-lab
```

5. If Jupyter Lab asks to select a kernel, choose 'group25-env'

#### Running the analysis

1. Navigate to the analysis folder, and open heart_disease_predictor.ipynb in Jupyter Lab. Then run the notebook from top to bottom by using the top menu: Run -> Run All Cells.

2. To reproduce the PDF, in Jupyter Lab: File -> Save and Export Notebook As -> PDF. Note: Additional libraries related to LaTeX may be required. If you run into a problem reproducing the PDF, you can also output a HTML file. If there are further issues, feel free to reach out to the authors of this project via their GitHub accounts.

## License

The Heart Disease Predictor project materials are licensed under the MIT License. See [the license file](LICENSE) for more information. If re-using/re-mixing please provide attribution and link to this webpage.
