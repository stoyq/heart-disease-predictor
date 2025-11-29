# Heart Disease Predictor

- Authors: Johnson Chuang | Eduardo Sanches | Azadeh Ramesh | Jose Davila

Data analysis and workflow project for DSCI 522 (Data Science Workflows), a course in the Master of Data Science program at the University of British Columbia.

## Summary

In this project, we use the UCI Heart Disease dataset to build a machine-learning model that predicts whether a patient is likely to have heart disease based on clinical and physiological attributes. Our results highlight key risk indicators that align with well-known medical knowledge, demonstrating how machine learning can support early screening and clinical decision-making.

## About the Dataset

The dataset that was used in this project can be found [here](https://archive.ics.uci.edu/dataset/45/heart+disease). It contains 303 observations, 14 features and a target value used to indicate the diagnosis of heart disease.

## Report

The final report can be found [here](doc/heart_disease_predictor.pdf).

## Dependencies

This project makes use of a host of external packages, and their specific version numbers can be found in the [environment.yml](environment.yml) file. We recommend using conda to reproduce the same environment for your platform, or using the Docker container that we provide.

## Setup

Follow the instructions below to reproduce the analysis.

Begin by cloning this GitHub repository.

```
git clone git@github.com:stoyq/heart-disease-predictor.git
```

Navigate to the `heart-disease-predictor` folder.

From here, you can either set up the environment locally on your computer (Method A), or use the Docker container that we provide (Method B).


#### Method A: Set up local installation

1. Create the environment from Makefile

    ```
    make env
    ```

2. Once the environment has been created, activate the environment

    ```
    conda activate group25-env
    ```

3. Run Jupyter Lab

    ```
    jupyter-lab
    ```

5. If Jupyter Lab asks to select a kernel, choose `group25-env`

#### Method B: Use the Docker container

1. After cloning the repository, launch the environment with:

    ```
    make up
    ```
    This will:

    - Try to pull the latest image from the team's DockerHub
    - Start a Jupyter Lab server inside the container
    - Mount the project directory into the container

2. Once the container starts, open the following address in your browser:

    <http://localhost:8899>

3. Run the analysis (next section). When finished, go back to the terminal and press:

    ```
    Ctrl + C
    ```

    Then stop the running container:

    ```
    docker compose stop
    ```

## Running the analysis

1. Navigate to the `analysis` folder, and open `heart_disease_predictor.ipynb` in Jupyter Lab. Then run the notebook from top to bottom by using the top menu: Run -> Run All Cells.

2. To reproduce the PDF, in Jupyter Lab: File -> Save and Export Notebook As -> PDF. Note: Additional libraries related to LaTeX may be required. If you run into a problem reproducing the PDF, you can also output a HTML file. If there are further issues, feel free to reach out to the authors of this project via their GitHub accounts.

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
