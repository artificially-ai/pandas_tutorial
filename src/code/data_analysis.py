"""
    Organisation: ekholabs
    Author: wilder.rodrigues@ekholabs.ai
"""

import matplotlib.pyplot as plt

from utils import dataset as ds

'''
    Let's start with loading out 'gapminder' dataset.
'''
DF = ds.load_gapminder()

'''
    Let's now do somple simple statistical analysis on the data.
'''


def mean_life_expectancy(plot = False):
    average = DF.groupby('year')['lifeExp'].mean()
    print("Average of life expectancy:", '\n', average, '\n')

    if plot:
        average.plot()
        plt.show()

def life_exp_continent_percapt():
    average = DF.groupby(['year', 'continent'])[['lifeExp', 'gdpPercap']].mean()
    print("Average of life expectancy per continent and GDP percapta:", '\n', average, '\n')


def countries_per_continent():
    nr_countries = DF.groupby('continent')['country'].nunique()
    print('# of countries per continent:', '\n', nr_countries, '\n')


if __name__ == '__main__':
    mean_life_expectancy()
    life_exp_continent_percapt()
    countries_per_continent()