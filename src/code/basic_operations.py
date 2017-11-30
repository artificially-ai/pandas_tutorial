"""
    Organisation: ekholabs
    Author: wilder.rodrigues@ekholabs.ai
"""

from utils import dataset as ds

'''
    Let's start with loading out 'scientists' dataset.
'''
DF = ds.load_scientists()


def avg_age():
    print('Average age of scientists:', '\n', DF['Age'].mean(), '\n')


def max_age():
    print('Oldest scientist:', '\n', DF['Age'].max(), '\n')


def min_age():
    print('Yougest scientist:', '\n', DF['Age'].min(), '\n')


def std_age():
    print('Standard deviation of scientists:', '\n', DF['Age'].std(), '\n')


def describe():
    print('Describe scientists ages:', '\n', DF['Age'].describe(), '\n')


def above_average():
    scientists_ages = DF[['Name', 'Age']]
    print('Age of scientists above average:', '\n', scientists_ages[scientists_ages['Age'] > scientists_ages['Age'].mean()], '\n')


if __name__ == '__main__':
    avg_age()
    max_age()
    min_age()
    std_age()
    describe()
    above_average()