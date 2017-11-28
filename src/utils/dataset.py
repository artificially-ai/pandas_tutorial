"""
    Organisation: ekholabs
    Author: wilder.rodrigues@ekholabs.ai
"""

import pandas as pd

PATH  = '../../data/'


def load_gapminder():
    return pd.read_csv(PATH + 'gapminder.tsv', sep = '\t')


def load_scientists():
    return pd.read_csv(PATH + 'scientists.csv')