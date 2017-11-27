import pandas as pd

PATH  = '../../data/'

'''
    Loads the "gapminder.tsv" dataset file and returns it as a DataFrme object.
'''
def load_gapminder():
    return pd.read_csv(PATH + 'gapminder.tsv', sep = '\t')

def load_scientists():
    return pd.read_csv(PATH + 'scientists.csv')