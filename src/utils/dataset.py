import pandas as pd

PATH  = '../../data/gapminder.tsv'

'''
    Loads the "gapminder.tsv" dataset file and returns it as a DataFrme object.
'''
def load_gapminder():
    return pd.read_csv(PATH, sep = '\t')