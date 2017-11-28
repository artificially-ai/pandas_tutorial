"""
    Organisation: ekholabs
    Author: wilder.rodrigues@ekholabs.ai
"""

import pandas as pd
import random

from utils import dataset as ds

'''
    Let's start with loading out 'scientists' dataset.
'''
DF = ds.load_scientists()
DF_COPY = DF.copy()

random.seed(42)


def by_age():
    avg_age = DF[DF['Age'] > DF['Age'].mean()]
    print('Average scientist age:', '\n', avg_age, '\n')


def to_date():
    born  = pd.to_datetime(DF.Born, format = '%Y-%m-%d')
    died = pd.to_datetime(DF.Died, format = '%Y-%m-%d')
    print('Date of birth and death:', '\n', born, died, '\n')


def add_columns():
    born  = pd.to_datetime(DF_COPY.Born, format = '%Y-%m-%d')
    died = pd.to_datetime(DF_COPY.Died, format = '%Y-%m-%d')

    DF_COPY['born_dt'] = born
    DF_COPY['died_dt'] = died

    print('New DataFrame...', '\n', DF_COPY, '\n', 'and shape: ', DF_COPY.shape, '\n')


def shuffle_age():
    random.shuffle(DF_COPY['Age'])
    subset = DF_COPY[['Name', 'Age']]
    print('Age has been shuffled in place:', '\n', subset, '\n')


def add_age_in_days_column():
    DF_COPY['age_days_dt'] = DF_COPY['died_dt'] - DF_COPY['born_dt']
    print('New DataFrame...', '\n', DF_COPY, '\n', 'and shape: ', DF_COPY.shape, '\n')


def add_age_in_years_column():
    DF_COPY['age_years_dt'] = DF_COPY['age_days_dt'].astype('timedelta64[Y]')
    print('New DataFrame...', '\n', DF_COPY, '\n', 'and shape: ', DF_COPY.shape, '\n')


if __name__ == '__main__':
    by_age()
    to_date()
    add_columns()
    shuffle_age()
    add_age_in_days_column()
    add_age_in_years_column()