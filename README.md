# Heart Disease Predictor

- Authors: Johnson Chuang | Eduardo Sanches | Azadeh Ramesh | Jose Davila

Data analysis and workflow project for DSCI 522 (Data Science Workflows), a course in the Master of Data Science program at the University of British Columbia.

## Summary

In this project, we use the UCI Heart Disease dataset to build a machine-learning model that predicts whether a patient is likely to have heart disease based on clinical and physiological attributes. Our results highlight key risk indicators that align with well-known medical knowledge, demonstrating how machine learning can support early screening and clinical decision-making.

## About the Dataset

The dataset that was used in this project can be found [here](https://archive.ics.uci.edu/dataset/45/heart+disease). It contains 303 observations, 14 features and a target value used to indicate the diagnosis of heart disease.

## Report

The final report can be found [here](doc/heart_disease_predictor_quarto_report.pdf).

## Project Environment and Dependencies

This project makes use of a host of external packages, and their specific version numbers can be found in the [environment.yml](environment.yml) file. We recommend using conda to reproduce the same environment for your particular platform, or using the Docker container that we provide.

## Setup

Follow the instructions below to reproduce the analysis.

Begin by cloning this GitHub repository.

```
git clone git@github.com:stoyq/heart-disease-predictor.git
```

Navigate to the `heart-disease-predictor` folder.

From here, you can either set up the environment locally on your computer (Method A), or use the Docker container that we provide (Method B).


#### Method A: Set up local environment

1. Create the environment from Makefile

    ```
    make env
    ```

2. Once the environment has been created, activate the environment

    ```
    conda activate group25-env
    ```

#### Method B: Use the Docker container

1. First ensure that Docker Desktop application is running, then from the terminal run:

    ```
    make up
    ```
    This will:

    - Try to pull the latest image from the team's DockerHub
    - Start a Jupyter Lab server inside the container
    - Mount the project directory into the container

2. Once the container starts, open the following address in your browser:

    <http://localhost:8899>

3. This will start Jupyter Lab. Click on Terminal icon and navigate to the root of the project directory (you will know you are at the root of the project if `ls` shows the same files as you see above. Once you are at the root of the project, you are ready to run the analysis (next section). When finished, go back to the terminal (where you typed `make up`) to stop the running container by:

    ```
    make stop
    ```

## Running the analysis

1. You can run the analysis by:

    ```
    make analysis
    ```
    This will download the dataset, perform cleaning, preprocessing, analysis, and output relevant tables and figures.

    Note: If you are running this inside the Docker container terminal (via Method B), and it says make command not found, then you can install make utility by:

    ```
    apt-get update
    apt-get install -y make
    ```

3. After running the analysis, you can reproduce the final project report by:

    ```
    make report
    ```
    This will use quarto to render out the .qmd file to both PDF and HTML format.

## How to contribute and update the Docker image

Using Docker ensures:

- Full reproducibility
- Identical environments for all team members
- No dependency conflicts
- Cross-platform support (macOS, Windows, Linux)
- Cleaner workflow compared to local conda environments

Our Docker image is automatically built and published through GitHub Actions to:

<https://hub.docker.com/r/josedmyt/heart-disease-predictor/tags>

Any changes to the `Dockerfile` or `conda-lock.yml` trigger an automated rebuild and publish to DockerHub. This ensures all team members always use the latest reproducible environment.

Libraries are frequently tested to ensure compatibility across all platforms. If you add a new package to the project, first add it to `environment.yml` with the correct cross-platform compatible version number. Then recreate the `conda-lock.yml` file by running:

```
make cl
```



## License

The Heart Disease Predictor project materials are licensed under the MIT License. See [the license file](LICENSE) for more information. If re-using/re-mixing please provide attribution and link to this webpage.
