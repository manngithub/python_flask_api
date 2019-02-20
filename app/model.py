# Importing the libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import requests
import json
import io


def build_sample_model():
    """
    This function takes salary dataset from public github location and train a linear regression
    model with training data and generate a serialized pickle model
    """
    
    # Importing the dataset
    dataset = pd.read_csv("https://raw.githubusercontent.com/vyashemang/flask-salary-predictor/master/Salary_Data.csv")
    
    # define features and response variables
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, 1].values
    
    # Splitting the dataset into the Training set and Test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 5)
    
    # Creating a Simple Linear Regression Model Object
    regressor = LinearRegression()
    
    # Fitting Simple Linear Regression to the Training set
    regressor.fit(X_train, y_train)
    
    # Optional: Predicting the Test set results
    y_pred = regressor.predict(X_test)
    
    # Saving model to disk
    pickle.dump(regressor, open('model.pkl','wb'), protocol=2)
    
    # Loading model to compare the results
    model = pickle.load(open('model.pkl','rb'))
    
    return model

if __name__ == '__main__':
    model = build_sample_model()
