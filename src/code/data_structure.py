'''
    Organisation: ekholabs
    Author: wilder.rodrigues@ai.com
'''

import pandas as pd

'''
    Let's now use Pandas' Series and DataFrames to create our own data structures.
'''

def create_series():
    fruits = pd.Series(['Banana', 'Kilo', .63])
    print('Fruits Series:', '\n', fruits, '\n')

def create_dataframe():
    dict = {'Product' : ['Banana', 'Water', 'Apple', 'Meat', 'Milk'],
            'Unit' : ['Kilo', 'Bottle', 'Kilo', 'Kilo', 'Bottle'],
            'Price' : [1.20, .55, 1.48, 15.90, .99]}
    basket = pd.DataFrame(dict)
    print('DataFrame head:', '\n', basket.head(), '\n')

def reindex_dataframe():
    dict = {'Unit' : ['Kilo', 'Bottle', 'Kilo', 'Kilo', 'Bottle'],
            'Price' : [1.20, .55, 1.48, 15.90, .99]}
    basket = pd.DataFrame(dict, index = ['Banana', 'Water', 'Apple', 'Meat', 'Milk'], columns = ['Unit', 'Price'])
    print('Reindex DataFrame head:', '\n', basket.head(), '\n')

if __name__ == '__main__':
    create_series()
    create_dataframe()
    reindex_dataframe()