import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys
import logging
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from logging_code import setup_logging
logger = setup_logging('feature_scalling')
from sklearn.preprocessing import StandardScaler # z score
from all_models import common
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import AdaBoostClassifier
import pickle

def fs(x_train, y_train, x_test, y_test):
    try:
        logger.info(f'training data independent size: {x_train.shape}')
        logger.info(f'training data dependent size: {y_train.shape}')
        logger.info(f'testing data independent size: {x_test.shape}')
        logger.info(f'testing data dependent size: {y_test.shape}')
        logger.info(f'before : {x_train.head(1)}')

        #  1. Scaling
        sc = StandardScaler()
        x_train_scaled = sc.fit_transform(x_train)
        x_test_scaled = sc.transform(x_test)

        # Convert to DataFrame
        x_train_scaled = pd.DataFrame(x_train_scaled, columns=x_train.columns)
        x_test_scaled = pd.DataFrame(x_test_scaled, columns=x_test.columns)

        #  CALL COMMON FUNCTION HERE
        common(x_train_scaled, y_train, x_test_scaled, y_test)

        # Save scaler
        with open('standar_Scaler.pkl', 'wb') as f:
            pickle.dump(sc, f)

        #  2. Model Training (USE BALANCED DATA)
        lr = LogisticRegression(max_iter=1000)
        model = AdaBoostClassifier(estimator=lr, n_estimators=5)

        model.fit(x_train_scaled, y_train)

        #  3. Save model
        with open('model.pkl', 'wb') as f:
            pickle.dump(model, f)

        logger.info("================ Model saved successfully =====================")

        # columns file is to refix the columns in backend code
        with open('columns.pkl', 'wb') as f:
            pickle.dump(x_train.columns, f)

        #  4. Evaluation
        y_pred = model.predict(x_test_scaled)

        logger.info(f'Accuracy: {accuracy_score(y_test, y_pred)}')
        logger.info(f'Confusion Matrix:\n{confusion_matrix(y_test, y_pred)}')
        logger.info(f'Report:\n{classification_report(y_test, y_pred)}')

        return x_train_scaled, y_train, x_test_scaled, y_test

    except Exception as e:
        er_type, er_msg, er_line = sys.exc_info()
        logger.info(f'Error in line no : {er_line.tb_lineno} due to : {er_msg}')

        return x_train, y_train, x_test, y_test