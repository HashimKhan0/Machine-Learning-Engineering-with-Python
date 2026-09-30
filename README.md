# Machine Learning Engineering with Python

Notes and worked examples from *Machine Learning Engineering with Python* (2nd ed.) by Andrew P. McMahon. The book focuses on taking ML models from notebook to production: project organization, the development process and CI/CD.

## Contents

### Chapter 1: Introduction to ML Engineering (`intro-to-ml-eng/`)

| File | Example |
|---|---|
| `Intro_to_ML_Engineering.md` | Chapter notes |
| `classification_example.py` | Random forest classifier with SMOTE class rebalancing and `RandomizedSearchCV` hyperparameter tuning |
| `clustering_example.py` | Simulated taxi-ride data (distance/speed) clustered with DBSCAN to flag anomalous rides |
| `forecasting_example.py` | Rossmann store-sales forecasting with Prophet (data pulled via the Kaggle API) |

### Chapter 2: The ML Development Process (`ml-dev-process/`)

| File | Contents |
|---|---|
| `The_ML_Dev_Process.md` | Notes on organizing ML projects, tooling for each stage, and CI/CD with GitHub Actions |
| `.github/workflows/github-actions-basic.yml` | Example CI workflow: Python 3.9/3.10 matrix, flake8 linting, pytest |

## Tech stack

Python · scikit-learn · imbalanced-learn · Prophet · pandas · NumPy · GitHub Actions
