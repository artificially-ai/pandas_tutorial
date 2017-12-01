"""
    Organisation: ekholabs
    Author: wilder.rodrigues@ekholabs.ai
"""

import pandas as pd

PATH  = '../../data/'


def load_gapminder(keep_default_na=True):
    return pd.read_csv(PATH + 'gapminder.tsv', sep = '\t', keep_default_na=keep_default_na)


def load_scientists(keep_default_na=True):
    return pd.read_csv(PATH + 'scientists.csv', keep_default_na=keep_default_na)


def load_survey(filename, keep_default_na=True):
    return pd.read_csv(PATH + filename, keep_default_na=keep_default_na)

def load_ebola(keep_default_na=True):
    return pd.read_csv(PATH + 'ebola_country_timeseries.csv', keep_default_na=keep_default_na)