import numpy as np
import pandas as pd
import os
import sys
import logging

from select import error

from logging_code import setup_logging
logger = setup_logging('cat_to_num')

from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder
import warnings
warnings.filterwarnings('ignore')

def c_t_n(x_train_cat, x_test_cat):

    try:
        logger.info(f'Before x_train_cat shape : {x_train_cat.shape} : \n : {x_train_cat.columns}')
        logger.info(f'Before x_test_cat shape : {x_test_cat.shape} : \n : {x_test_cat.columns}')

        # Separate Ordinal column and nominal columns

        y_train = x_train_cat[['Contract']]  # ordinal data
        y_test = x_test_cat[['Contract']]

        x_train_cat = x_train_cat.drop(['Contract'], axis=1)  # nominal data
        x_test_cat = x_test_cat.drop(['Contract'], axis=1)

        # Find Binary and Multi-category columns

        binary_cols = []
        multi_cols = []

        for col in x_train_cat.columns:
            if x_train_cat[col].nunique() <= 2:
                binary_cols.append(col)
            else:
                multi_cols.append(col)

        logger.info(f'Binary columns : {binary_cols}')
        logger.info(f'Multi category columns : {multi_cols}')

        # One-Hot Encoding for Binary Columns

        one_hot_bin = OneHotEncoder(drop='first', sparse_output=False)

        x_train_bin = one_hot_bin.fit_transform(x_train_cat[binary_cols])
        x_test_bin = one_hot_bin.transform(x_test_cat[binary_cols])

        x_train_bin = pd.DataFrame(
            x_train_bin,
            columns=one_hot_bin.get_feature_names_out(binary_cols),
            index=x_train_cat.index
        )

        x_test_bin = pd.DataFrame(
            x_test_bin,
            columns=one_hot_bin.get_feature_names_out(binary_cols),
            index=x_test_cat.index
        )

        # one hot encoding for Multi category columns

        one_hot_multi = OneHotEncoder(drop='first', sparse_output=False)

        x_train_multi = one_hot_multi.fit_transform(x_train_cat[multi_cols])
        x_test_multi = one_hot_multi.transform(x_test_cat[multi_cols])

        x_train_multi = pd.DataFrame(
            x_train_multi,
            columns=one_hot_multi.get_feature_names_out(multi_cols),
            index=x_train_cat.index
        )

        x_test_multi = pd.DataFrame(
            x_test_multi,
            columns=one_hot_multi.get_feature_names_out(multi_cols),
            index=x_test_cat.index
        )

        # combine both binary and multi columns

        x_train_final = pd.concat([x_train_bin, x_train_multi], axis=1)
        x_test_final = pd.concat([x_test_bin, x_test_multi], axis=1)

        logger.info(f'After encoding train shape : {x_train_final.shape}')
        logger.info(f'After encoding test shape : {x_test_final.shape}')

        # Ordinal Encoding for ordinal data

        od = OrdinalEncoder()

        y_train_encoded = od.fit_transform(y_train)
        y_test_encoded = od.transform(y_test)

        y_train_encoded = pd.DataFrame(
            y_train_encoded,
            columns=['Contract_Encoded'],
            index=y_train.index
        )

        y_test_encoded = pd.DataFrame(
            y_test_encoded,
            columns=['Contract_Encoded'],
            index=y_test.index
        )

        logger.info(f'Ordinal categories : {od.categories_}')


        x_train_final = pd.concat([x_train_final, y_train_encoded], axis=1)
        x_test_final = pd.concat([x_test_final, y_test_encoded], axis=1)

        logger.info(f'Final Train Shape : {x_train_final.shape} : \n : {x_train_final.columns}')
        logger.info(f'Final Test Shape : {x_test_final.shape} : \n : {x_test_final.columns}')


        return x_train_final, x_test_final

    except Exception as e:
        er_type, er_msg, er_line = sys.exc_info()
        logger.error(f'Error in line {er_line.tb_lineno} : {er_msg}')
        return x_train_cat, x_test_cat