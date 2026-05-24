import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import os
import sys
import logging
from logging_code import setup_logging
logger = setup_logging('var_transformation')
from sklearn.model_selection import train_test_split
import seaborn as sns
from sklearn.preprocessing import QuantileTransformer
from scipy.stats import yeojohnson
import scipy.stats as stats

def vt(x_train_num, x_test_num):
    try:
        logger.info('====================== variable transformation =================================')

        logger.info(f"Before Train Column Name : {x_train_num.columns}")
        logger.info(f"Before Test Column Name : {x_test_num.columns}")

        def fun(data, var):
            plt.figure(figsize=(10,4))
            plt.subplot(1, 3, 1)
            plt.title("Outliers")
            sns.boxplot(x=data[var])

            plt.subplot(1, 3, 2)
            plt.title("Normal Distribution")
            data[var].plot(kind='kde')

            plt.subplot(1, 3, 3)
            plt.title("probplot")
            stats.probplot(data[var], dist="norm", plot=plt)

            plt.show()


        for i in x_train_num.columns:
            if 'SeniorCitizen' != i:
                if i == 'tenure':
                    new_col = i +'_yeo'
                    x_train_num[new_col], lam_val = yeojohnson(x_train_num[i])
                    x_test_num[new_col] = yeojohnson(x_test_num[i], lmbda=lam_val)
                    fun(x_train_num, new_col)
                    x_train_num = x_train_num.drop(i, axis=1)
                    x_test_num = x_test_num.drop(i, axis=1)
                else:
                    quantile_trans = QuantileTransformer(output_distribution='normal')
                    new_col1 = i +'_quantile'
                    x_train_num[new_col1] = quantile_trans.fit_transform(x_train_num[[i]])
                    x_test_num[new_col1] = quantile_trans.fit_transform(x_test_num[[i]])
                    fun(x_train_num, new_col1)
                    x_train_num = x_train_num.drop(i, axis=1)
                    x_test_num = x_test_num.drop(i, axis=1)


        logger.info(f"After Train Column Name : {x_train_num.columns}")
        logger.info(f"After Test Column Name : {x_test_num.columns}")

        return x_train_num,x_test_num

    except Exception as e:
        er_type, er_msg, er_line = sys.exc_info()
        logger.info(f'Error in line no : {er_line.tb_lineno} due to : {er_msg}')

        return x_train_num, x_test_num



def handle_outlier(x_train_num, x_test_num):
    try:
        logger.info('================== Handling Outlier =========================')

        logger.info(f"Before Train Column Name : {x_train_num.columns}")
        logger.info(f"Before Test Column Name : {x_test_num.columns}")

        def fun1(data, var):
            plt.figure(figsize=(5, 3))
            sns.boxplot(x=data[var])
            plt.title(var)
            plt.show()

        for col in list(x_train_num.columns):
            if col != 'SeniorCitizen':

                iqr = x_train_num[col].quantile(0.75) - x_train_num[col].quantile(0.25)
                lower_limit = x_train_num[col].quantile(0.25) - (1.5 * iqr)
                upper_limit = x_train_num[col].quantile(0.75) + (1.5 * iqr)

                # create trimmed columns
                x_train_num[col + '_trim'] = np.where(
                    x_train_num[col] > upper_limit, upper_limit,
                    np.where(x_train_num[col] < lower_limit, lower_limit, x_train_num[col])
                )

                x_test_num[col + '_trim'] = np.where(
                    x_test_num[col] > upper_limit, upper_limit,
                    np.where(x_test_num[col] < lower_limit, lower_limit, x_test_num[col])
                )
                # visualize
                fun1(x_train_num, col + '_trim')

                # drop original column
                x_train_num.drop(col, axis=1, inplace=True)
                x_test_num.drop(col, axis=1, inplace=True)

        #  keep only '_trim' columns + 'SeniorCitizen'
        train_cols = [col for col in x_train_num.columns if col.endswith('_trim')]
        test_cols = [col for col in x_test_num.columns if col.endswith('_trim')]

        if 'SeniorCitizen' in x_train_num.columns:
            train_cols.append('SeniorCitizen')
        if 'SeniorCitizen' in x_test_num.columns:
            test_cols.append('SeniorCitizen')

        x_train_num = x_train_num[train_cols]
        x_test_num = x_test_num[test_cols]

        logger.info(f"After Train Column Name : {x_train_num.columns}")
        logger.info(f"After Test Column Name : {x_test_num.columns}")

        return x_train_num, x_test_num

    except Exception as e:
        er_type, er_msg, er_line = sys.exc_info()
        logger.error(f'Error in line no : {er_line.tb_lineno} due to : {er_msg}')

        return x_train_num, x_test_num