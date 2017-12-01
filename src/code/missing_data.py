"""
    Organisation: ekholabs
    Author: wilder.rodrigues@ekholabs.ai
"""

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


if __name__ == '__main__':
    create_dataframe_nan_values()
    create_dataframe_na_values()
    load_datasets_nan_na_values()