'''
    Organisation: ekholabs
    Author: wilder.rodrigues@ai.com
'''
import pandas as pd

from utils import dataset as ds

'''
    Let's start with loading out 'scientists' dataset.
'''
DF = ds.load_scientists()

def by_age():
    avg_age = DF[DF['Age'] > DF['Age'].mean()]
    print('Average scientist age:', '\n', avg_age, '\n')

def to_date():
    born  = pd.to_datetime(DF.Born, format = '%Y-%m-%d')
    died = pd.to_datetime(DF.Died, format = '%Y-%m-%d')
    print('Date of birth and death:', '\n', born, died, '\n')

if __name__ == '__main__':
    by_age()
    to_date()