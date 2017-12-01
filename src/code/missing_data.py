"""
    Organisation: ekholabs
    Author: wilder.rodrigues@ekholabs.ai
"""

import numpy as np
import pandas as pd

from utils import dataset as ds
from numpy import NaN, nan, NAN

'''
    Inside the visited = ds.load_survey('survey_visited.csv', keep_default_na=True) function you will see the following line:
        pd.read_csv(PATH + filename, keep_default_na=keep_default_na)
'''


def load_default_na_on():
    visited = ds.load_survey('survey_visited.csv', keep_default_na=True)
    print('Dataframe with NaN values:', '\n', visited, '\n')


def load_default_na_off():
    visited = ds.load_survey('survey_visited.csv', keep_default_na=False)
    print('Dataframe without NaN values:', '\n', visited, '\n')


def create_dataframe_nan_values():
    scientists = ds.load_scientists()

    # Create a boolean array where True means the age is above average and False otherwise.
    ages = scientists['Age']
    cond = [x > ages.mean() for x in ages.values]

    # Replace ages below average with NaN
    scientists['Age'].where(cond, other=NaN, inplace=True)

    # Save the DataFrame as a CSV file
    scientists.to_csv('../../data/test/scientists_NaN_values.csv', index=False)


def create_dataframe_na_values():
    scientists = ds.load_scientists()

    # Create a boolean array where True means the age is above average and False otherwise.
    ages = scientists['Age']
    cond = [x > ages.mean() for x in ages.values]

    # Replace ages below average with NA, which is not NaN.
    scientists['Age'].where(cond, other='NA', inplace=True)

    scientists.to_csv('../../data/test/scientists_NA_values.csv', index=False)

def load_datasets_nan_na_values():
    # This won't show NaN values, but empty instead: keep_default_na=False
    scientists_nan = pd.read_csv('../../data/test/scientists_NaN_values.csv', keep_default_na=False)
    print('Scientists without NaN values:', '\n', scientists_nan, '\n')

    # This WILL show NA values bacause we specified 'na_values' as containing only NaN, which is
    # not the case for this file.
    scientists_na = pd.read_csv('../../data/test/scientists_NA_values.csv', na_values=[NaN], keep_default_na=False)
    print('Scientists with NA values:', '\n', scientists_na, '\n')

    # This won't show NA values, but empty instead: na_values=['NA'] and keep_default_na=False
    scientists_na = pd.read_csv('../../data/test/scientists_NA_values.csv', na_values=['NA'])
    print('Scientists without NA values:', '\n', scientists_na, '\n')


def count_missing_data():
    ebola = ds.load_ebola()
    print('Eboda data:', '\n', ebola.head(), '\n')
    print('# of entries per column:', '\n', ebola.count(), '\n')

    num_rows = ebola.shape[0]
    num_missing = num_rows - ebola.count()
    print('# of missing entries per column:', '\n', num_missing, '\n')


def count_missing_values_numpy():
    ebola = ds.load_ebola()
    print('Eboda data:', '\n', ebola.head(), '\n')

    missing_values = np.count_nonzero(ebola.isnull())
    print('Missing values in DataFrame:', '\n', missing_values, '\n')

    missing_values = np.count_nonzero(ebola['Cases_Guinea'].isnull())
    print('Missing values in Series:', '\n', missing_values, '\n')

    # NaN values will be on the top, so look at the head()
    missing_values = ebola['Cases_Guinea'].value_counts(dropna=False).head()
    print('Missing values in Series II:', '\n', missing_values, '\n')


def fill_missing_values():
    ebola = ds.load_ebola()
    # Fills missing values with the value on the previous row. In case the previous row is NaN, it doesn't do anything.
    # We can also use fillna(0, inplace=True) to change the current DataFrame. It will avoid creating a copy
    print('Ebola data:', '\n', ebola.fillna(0).ix[0:10, 0:5], '\n')


def forward_fill_missing_values():
    ebola = ds.load_ebola()
    # Fills values with the vLAST valid observation. In case the previous row is NaN, it doesn't do anything.
    # Observe the column 'Cases_Liberia' and the rows 2 and 3
    print('Ebola data:', '\n', ebola.fillna(method='ffill').ix[0:10, 0:5], '\n')


def backward_fill_missing_values():
    ebola = ds.load_ebola()
    # Fills missing values with the NEXT valid observation. In case the previous row is NaN, it doesn't do anything.
    # Observe the column 'Cases_Liberia' and the rows 2 and 3
    print('Ebola data:', '\n', ebola.fillna(method='bfill').ix[0:, 0:5].head(), '\n')
    print('Ebola data:', '\n', ebola.fillna(method='bfill').ix[0:, 0:5].tail(), '\n')


def drop_nan_values():
    ebola = ds.load_ebola()
    # One can also drop rows with NaN values, but that has to be done with caution.
    # If we drop the th NaN values form the ebola DataFrame, we will end up with only one row.
    # It returns a new DataFrame, unless we use inplace=True
    print('Dropping NaN values:', '\n', ebola.dropna().shape)


if __name__ == '__main__':
    drop_nan_values()