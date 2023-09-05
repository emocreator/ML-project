# ML-project

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

## Notes

- This project demonstrates how to structure a ML project with separation of concerns between components.
- Logging and exception handling is done using custom logger and exception classes.
- Ideal for learning how modular ML projects are built.
- Can be extended to include more components like model evaluation, deployment etc.

Let me know if you would like any clarification or changes in this README!