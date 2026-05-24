import numpy as np
import pandas as pd
import sys
import logging
from logging_code import setup_logging
logger = setup_logging('filter_methods')

from sklearn.feature_selection import VarianceThreshold
from scipy.stats import pearsonr


def filter(x_train, x_test, y_train, y_test):
    try:
        logger.info(f'Before Train Shape : {x_train.shape} : {x_train.columns}')
        logger.info(f'Before Test Shape : {x_test.shape} : {x_test.columns}')


        #  1. Variance Threshold

        reg = VarianceThreshold(threshold=0.01)
        reg.fit(x_train)

        x_train = x_train.loc[:, reg.get_support()]
        x_test = x_test.loc[:, reg.get_support()]

        logger.info(f'After Variance Threshold : {x_train.shape}')

        # 2. Hypothesis Testing (p-value)

        selected_cols = []

        for col in x_train.columns:
            try:
                corr, p_val = pearsonr(x_train[col], y_train)

                if p_val < 0.05:   # important feature
                    selected_cols.append(col)

            except:
                # keep column if error (safe)
                selected_cols.append(col)

        x_train = x_train[selected_cols]
        x_test = x_test[selected_cols]

        logger.info(f'After P-value Selection : {x_train.shape}')

        logger.info(f'Final Train Shape : {x_train.shape} : {x_train.columns}')
        logger.info(f'Final Test Shape : {x_test.shape} : {x_test.columns}')

        return x_train, x_test

    except Exception as e:
        er_type, er_msg, er_line = sys.exc_info()
        logger.error(f'Error in line {er_line.tb_lineno} : {er_msg}')

