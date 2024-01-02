import pandas as pd 
import numpy as np 
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV
from imblearn.over_sampling import SMOTE

'''
    the function below reads our data into a pandas dataframe
    splits the data into training and testing
    one hot encodes the training features
    returns all the train and test features and targets
'''
def ingest_and_prep_data(
        bank_dataset: str = 'bank.csv'
        ) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame,
                   pd.DataFrame]:
    df = pd.read_csv('bank.csv', delimiter=';',
                      decimal=',')
    
    feature_cols = ['job', 'marital', 'education', 'contact',
                    'housing', 'loan', 'default', 'day']
    X = df[feature_cols].copy()
    y = df['y'].apply(lambda x: 1 if x == 'yes' else 0).copy()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    enc = OneHotEncoder(handle_unknown='ignore')
    X_train = enc.fit_transform(X_train)
    return X_train, X_test, y_train, y_test

'''
    Because the data is imbalanced we need to rebalance the training data with an oversampling technique
    here we use Synthetic Minority Over-Sampling Technique (SMOTE) from imblearn
'''

def rebalance_classes(X: pd.DataFrame, y: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    sm = SMOTE()
    X_balanced, y_balanced = sm.fit_resample(X, y)
    return X_balanced, y_balanced

'''
    Now we will move onto the main ML components of the script
    we will perform a hyperparameter search 
'''

def get_hyperparam_grid() -> dict:
    n_estimators = [int(x) for x in np.linspace(start=200,
                    stop=2000, num=10)]
    max_features = ['auto', 'sqrt']
    max_depth = [int(x) for x in np.linspace(10, 110, num=11)]
    max_depth.append(None)
    min_samples_split = [2, 5, 10]
    min_samples_leaf = [1, 2, 4]
    bootstrap = [True, False]  # Create the random grid
    random_grid = {
        'n_estimators': n_estimators,
        'max_features': max_features,
        'max_depth': max_depth,
        'min_samples_split': min_samples_split,
        'min_samples_leaf': min_samples_leaf,
        'bootstrap': bootstrap
    }
    return random_grid

'''
    Finally this grid of hyperparameters will be used in the definition of a RandomisedSearchCV object to otpimize an estimator over the hyperparameter values
'''

def get_randomised_rf_cv(random_grid: dict) -> sklearn.model_selection._search.RandomizedSearchCV:
    # Use the random grid to search for best hyperparameters
    # First create the base model to tune
    rf = RandomForestClassifier()
    # Random search of parameters, using 3 fold cross validation,
    # search across 100 different combinations, and use all available cores
    rf_random = RandomizedSearchCV(
        estimator=rf,
        param_distributions=random_grid,
        n_iter=100,
        cv=3,
        verbose=2,
        random_state=42,
        n_jobs=-1,
        scoring='f1'
    )
    return rf_random

'''
    the main block of the script
    1) reads the data
    2) rebalances the training set
    3) executes a hyperparameter optimized run on a randomized grid search for a random forest classifier
'''
if __name__ == "__main__":
    X_train, X_test, y_train, y_test = ingest_and_prep_data()
    X_balanced, y_balanced = rebalance_classes(X_train, y_train)
    rf_random = get_randomised_rf_cv(
                  random_grid=get_hyperparam_grid()
                  )
    rf_random.fit(X_balanced, y_balanced)