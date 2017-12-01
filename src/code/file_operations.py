"""
    Organisation: ekholabs
    Author: wilder.rodrigues@ekholabs.ai
"""

from utils import dataset as ds

'''
    Let's start with loading out 'scientists' dataset.
'''
scientists = ds.load_scientists()

def save_to_pickle():
    scientists.to_pickle('../../data/test/scientists.pickle')


def save_to_csv():
    scientists.to_csv('../../data/test/scientists.csv', index=False)


def save_to_tsv():
    scientists.to_csv('../../data/test/scientists.tsv', sep = '\t')


def save_to_excel():
    scientists.to_excel('../../data/test/scientists.xlsx', index = False)


if __name__ == '__main__':
    save_to_pickle()
    save_to_csv()
    save_to_tsv()
    save_to_excel()