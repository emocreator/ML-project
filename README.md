1. Firstly Create your new Environment

```conda create -p env python=3.9 -y```

2. Activate Conda Environment

```conda activate env/``` -> CMD

```source activate env/``` -> Git bash

3. Install necessary requirements

```pip install -r requirements.txt```

Here is a README.md for the project:

# Delivery Time Prediction Project

This is a machine learning project to predict delivery times based on various features like traffic, weather etc. It follows a modular structure for easy maintenance.

## Project Structure

```
- src
  - components
    - data_ingestion.py
    - data_transformation.py 
    - model_trainer.py
  - config
    - configuration.py
  - constants
    - constants.py
  - exception
    - exception.py
  - logger
    - logger.py
  - pipeline
    - training_pipeline.py
  - utils
    - __init__.py
- artifacts
- data
- logs
- notebooks
- README.md
```

## Usage

The main entry point is `training_pipeline.py`. It does the following:

1. Calls `data_ingestion.py` to split the raw data into train and test sets.
2. Calls `data_transformation.py` to preprocess the data and engineer features.
3. Calls `model_trainer.py` to train and evaluate models. It saves the best model.
4. Configuration parameters are stored in `config/configuration.py`.
5. Logger and custom exceptions are handled in `logger.py` and `exception.py`. 
6. Common utility functions are kept in `utils.py`.

The output model and intermediate artifacts are saved in the `artifacts` folder.

## How to run Prediction

```bash
python src/components/data_ingestion.py
```

This will do all the steps and generate the model file in `artifacts/model_trainer`.

## How to make predictions

```bash
python prediction/batch.py
```

## Dataset

The dataset used for this project is `data/finalTrain.csv`. It contains the following features:

- ID: Unique ID for each row
- Type_of_order: Online or offline order
- Type_of_vehicle: Bike, Car etc.
- Time_taken: Target variable, delivery time in minutes.

## Data Ingestion

The `data_ingestion.py` does the following:

- Load data from csv file
- Split into train and test sets
- Save train and test csv files in the `artifacts/data_ingestion` folder.

## Data Transformation 

The main steps done in `data_transformation.py`:

- Handle missing values
- Encode categorical features
- Standardize numerical columns
- Engineer new features like distance calculation
- Save the transformed data in `artifacts/data_transformation` folder.

It also saves the preprocessing object for use during prediction.

## Model Training

`model_trainer.py` trains the following regression models:

- XGBRegressor
- RandomForestRegressor
- SVM

It evaluates them based on R2 score and saves the best model to `artifacts/model_trainer`.

## Deployment 

The model can be deployed using Flask by creating a `app.py` file that loads the model and serves predictions via an API.

## Monitoring

The model's performance can be monitored in production by tracking live metrics like request throughput, latency, error rates etc.

## Notes

- This project demonstrates how to structure a ML project with separation of concerns between components.
- Logging and exception handling is done using custom logger and exception classes.
- Ideal for learning how modular ML projects are built.
- Can be extended to include more components like model evaluation, deployment etc.
