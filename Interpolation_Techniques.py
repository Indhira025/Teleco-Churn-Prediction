import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import sys
import logging
from logging_code import setup_logging
logger = setup_logging('Interpolation_Techniques')

def handling_missing_values(x_train,x_test):
    try:
        logger.info(f'Before handling null values x_train column names and shape : {x_train.shape} : \n : {x_train.columns} : {x_train.isnull().sum()}')
        logger.info(f'Before handling null values x_test column names and shape : {x_test.shape} : \n : {x_test.columns}: {x_test.isnull().sum()}')

        for i in x_train.columns:
            if x_train[i].isnull().sum() > 0:
                x_train[i+'_interpolate'] = x_train[i].interpolate(method='linear')
                x_test[i+'_interpolate'] = x_test[i].interpolate(method='linear')
                x_train = x_train.drop([i],axis=1)
                x_test = x_test.drop([i], axis=1)

        logger.info(f'After handling null values x_train column names and shape : {x_train.shape} : \n : {x_train.columns} : {x_train.isnull().sum()}')
        logger.info(f'After handling null values x_test column names and shape : {x_test.shape} : \n : {x_test.columns}: {x_test.isnull().sum()}')

        return x_train, x_test

    except Exception as e:
        er_type, er_msg, er_line = sys.exc_info()
        logger.info(f'Error in line no : {er_line.tb_lineno} due to : {er_msg}')