'''
In this file I am going to call all related functions for data cleaning and model development
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys
import logging
from logging_code import setup_logging
logger = setup_logging('main')
from sklearn.model_selection import train_test_split
from Interpolation_Techniques import handling_missing_values
import seaborn as sns
from var_transformation import vt
from var_transformation import handle_outlier
from filter_methods import filter
from cat_to_num import c_t_n
from imblearn.over_sampling import SMOTE
from feature_scalling import fs
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import AdaBoostClassifier
import pickle


class CUSTOMER:
    def __init__(self,path):
        try:
            self.path = path
            self.df = pd.read_csv(path) # loading dataset
            logger.info(f'Before removing unwanted cols Total dataset_size: {self.df.shape}')
            self.df.drop(['customerID'], axis=1, inplace=True)  # removing unwanted columns
            logger.info(f'After removing Total dataset_size: {self.df.shape}')  # total columns after removing unwanted col
            logger.info('================= spliting data =========================')
            self.x = self.df.iloc[ : , :-1] # independent columns
            self.y = self.df.iloc[ : ,-1] # dependent column
            self.x_train,self.x_test,self.y_train,self.y_test = train_test_split(self.x,self.y,test_size=0.2,random_state=45) # spliting data
            self.y_train = self.y_train.str.strip().map({'Yes': 1, 'No': 0}).astype(int) # dependent column categores changed to num
            self.y_test = self.y_test.str.strip().map({'Yes': 1, 'No': 0}).astype(int)
            logger.info(f'Train data_size : {len(self.x_train) , len(self.y_train)}  : total train data : {self.x_train.shape}')
            logger.info(f'Test data_size : {len(self.x_test) , len(self.y_test)}  : total test data : {self.x_test.shape}')
            logger.info('============== checking for null values =====================')
            logger.info(f'Null Values: \n : {self.df.isnull().sum()}')  # checking for null values
        except Exception as e:
            er_type, er_msg, er_line = sys.exc_info()
            logger.info(f'Error in line no : {er_line.tb_lineno} due to : {er_msg}')

    def missing_values(self):
        try:
            for i in self.x_train.columns:
                if self.x_train[i].isnull().sum() > 0:
                    logger.info(f'{i} : {self.x_train[i].dtype}')

            logger.info('================== Handling Missing Values ======================')

            logger.info(f'Before handling null values x_train column names and shape : {self.x_train.shape} : \n : {self.x_train.columns} : {self.x_train.isnull().sum()}')
            logger.info(f'Before handling null values x_test column names and shape : {self.x_test.shape} : \n : {self.x_test.columns}: {self.x_test.isnull().sum()}')

            self.x_train,self.x_test = handling_missing_values(self.x_train,self.x_test)

            logger.info(f'After handling null values x_train column names and shape : {self.x_train.shape} : \n : {self.x_train.columns} : {self.x_train.isnull().sum()}')
            logger.info(f'After handling null values x_test column names and shape : {self.x_test.shape} : \n : {self.x_test.columns}: {self.x_test.isnull().sum()}')

        except Exception as e:
            er_type, er_msg, er_line = sys.exc_info()
            logger.info(f'Error in line no : {er_line.tb_lineno} due to : {er_msg}')

    def data_separation(self):
        try:
            logger.info('============= Data Separation ========================')

            self.x_train_num_cols = self.x_train.select_dtypes(exclude= 'object')
            self.x_test_num_cols = self.x_test.select_dtypes(exclude= 'object')

            self.x_train_cat_cols = self.x_train.select_dtypes(include=['object', 'string'])
            self.x_test_cat_cols = self.x_test.select_dtypes(include=['object', 'string'])

            logger.info(f'{self.x_train_num_cols.columns} : {self.x_train_num_cols.shape}')
            logger.info(f'{self.x_test_num_cols.columns} : {self.x_test_num_cols.shape}')
            logger.info(f'{self.x_train_cat_cols.columns} : {self.x_train_cat_cols.shape}')
            logger.info(f'{self.x_test_cat_cols.columns} : {self.x_test_cat_cols.shape}')

        except Exception as e:
            er_type, er_msg, er_line = sys.exc_info()
            logger.info(f'Error in line no : {er_line.tb_lineno} due to : {er_msg}')

    def variable_transformation(self):
        try:
            logger.info('=============== Variable Transformation ============================')

            logger.info(f"Before Train Column Name : {self.x_train_num_cols.columns}")
            logger.info(f"Before Test Column Name : {self.x_test_num_cols.columns}")

            self.x_train_num_cols, self.x_test_num_cols = vt(self.x_train_num_cols, self.x_test_num_cols)

            logger.info(f"After Train Column Name : {self.x_train_num_cols.columns}")
            logger.info(f"After Test Column Name : {self.x_test_num_cols.columns}")

            logger.info('=============== handling outlier ============================')

            logger.info(f"Before Train Column Name : {self.x_train_num_cols.columns}")
            logger.info(f"Before Test Column Name : {self.x_test_num_cols.columns}")

            self.x_train_num_cols, self.x_test_num_cols = handle_outlier(self.x_train_num_cols, self.x_test_num_cols)

            logger.info(f"After Train Column Name : {self.x_train_num_cols.columns}")
            logger.info(f"After Test Column Name : {self.x_test_num_cols.columns}")

        except Exception as e:
            er_type, er_msg, er_line = sys.exc_info()
            logger.info(f'Error in line no : {er_line.tb_lineno} due to : {er_msg}')


    def cat_to_num(self):
        try:
            logger.info('================== cat to num ================================')

            logger.info(f'Before x_train_cat shape : {self.x_train_cat_cols.shape} : \n : {self.x_train_cat_cols.columns}')
            logger.info(f'Before x_test_cat shape : {self.x_test_cat_cols.shape} : \n : {self.x_test_cat_cols.columns}')

            self.x_train_cat_cols, self.x_test_cat_cols = c_t_n(self.x_train_cat_cols,self.x_test_cat_cols)

            logger.info(f'After x_train_cat shape : {self.x_train_cat_cols.shape} : \n : {self.x_train_cat_cols.columns}')
            logger.info(f'After x_test_cat shape : {self.x_test_cat_cols.shape} : \n : {self.x_test_cat_cols.columns}')

            # combine cat and num columns
            logger.info('======================== combine cat and num cols =============================')

            self.x_train_num_cols.reset_index(drop=True, inplace=True)
            self.x_train_cat_cols.reset_index(drop=True, inplace=True)

            self.x_test_num_cols.reset_index(drop=True, inplace=True)
            self.x_test_cat_cols.reset_index(drop=True, inplace=True)

            self.training_data = pd.concat([self.x_train_num_cols,self.x_train_cat_cols],axis = 1)
            self.testing_data = pd.concat([self.x_test_num_cols,self.x_test_cat_cols],axis = 1)

            logger.info(f'Final Training data : {self.training_data.shape}')
            logger.info(f'{self.training_data.isnull().sum()}')

            logger.info(f'Final Testing data : {self.testing_data.shape}')
            logger.info(f'{self.testing_data.isnull().sum()}')

        except Exception as e:
            er_type, er_msg, er_line = sys.exc_info()
            logger.info(f'Error in line no : {er_line.tb_lineno} due to : {er_msg}')

    def feature_selection(self):
        try:
            logger.info('============== Feature Selection ===============================')

            logger.info(f'Before filter methods training data : {self.training_data.shape} : \n : {self.training_data.columns}')
            logger.info(f'Before filter methods Te4sting data: {self.testing_data.shape} : \n : {self.testing_data.columns}')

            self.training_data, self.testing_data = filter(self.training_data,self.testing_data,self.y_train,self.y_test)

            logger.info(f'after filter methods training data : {self.training_data.shape} : \n : {self.training_data.columns}')
            logger.info(f'after filter methods testing data: {self.testing_data.shape} : \n : {self.testing_data.columns} ')
        except Exception as e:
            er_type, er_msg, er_line = sys.exc_info()
            logger.info(f'Error in line no : {er_line.tb_lineno} due to : {er_msg}')


    def balance_data(self):
        try:
            logger.info('================== Balance data =================')

            logger.info(f'Good (1): {sum(self.y_train == 1)}')
            logger.info(f'Bad (0): {sum(self.y_train == 0)}')

            sm = SMOTE(random_state=42)

            self.training_data_bal, self.y_train_bal = sm.fit_resample(self.training_data, self.y_train)

            logger.info(f'Total row for Good category in training data {self.training_data_bal.shape[0]} was : {sum(self.y_train_bal == 1)}')
            logger.info(f'Total row for Bad category in training data {self.training_data_bal.shape[0]} was : {sum(self.y_train_bal == 0)}')

        except Exception as e:
            er_type, er_msg, er_line = sys.exc_info()
            logger.info(f'Error in line no : {er_line.tb_lineno} due to : {er_msg}')

    def feature_scaling(self):
        try:
            logger. info('===================== Feature Scaling =========================')

            logger.info(f'Before training data columns : {self.training_data_bal.shape} ')
            logger.info(f'Before testing data columns : {self.testing_data.shape} ')

            self.training_data_bal, self.y_train_bal, self.testing_data, self.y_test = fs(self.training_data_bal, self.y_train_bal,self.testing_data, self.y_test)

            logger.info(f'after training data columns :  {self.training_data_bal.shape} : \n : {self.training_data_bal.columns}')
            logger.info(f'after testing data columns : {self.testing_data.shape} : \n : {self.testing_data.columns}')


        except Exception as e:
            er_type, er_msg, er_line = sys.exc_info()
            logger.info(f'Error in line no : {er_line.tb_lineno} due to : {er_msg}')

if __name__ == '__main__':
    try:
        obj = CUSTOMER('Teleco_Customer_Churn.csv')
        obj.missing_values()
        obj.data_separation()
        obj.variable_transformation()
        obj.cat_to_num()
        obj.feature_selection()
        obj.balance_data()
        obj.feature_scaling()

    except Exception as e:
        er_type, er_msg, er_line = sys.exc_info()
        logger.info(f'Error in line no : {er_line.tb_lineno} due to : {er_msg}')
