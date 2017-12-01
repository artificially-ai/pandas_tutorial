"""
    Organisation: ekholabs
    Author: wilder.rodrigues@ekholabs.ai
"""

from utils import dataset as ds

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


if __name__ == '__main__':
    load_default_na_on()
    load_default_na_off()