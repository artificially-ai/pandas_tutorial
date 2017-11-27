'''
    Organisation: ekholabs
    Author: wilder.rodrigues@ai.com
'''

from utils import dataset as ds

'''
    Let's start with loading out 'gapminder' dataset.
'''
DF = ds.load_gapminder()

'''
    Let's explore some of the basic operartions of a Pandas' DataFrame.
    
        * DF.head(): returns the first 5 rows of a DataFrame.
        * type(DF): it's a Python function that returns the type of an object.
        * DF.shape: returns the shape of a DataFrame. It's not a functon, but an attribute.
        * DF.dtypes: returns the data types of the Pandas' DataFrame. It's not a functon, but an attribute.
        * DF.info(): returns information concerning the structure of the DataFrame.
        * DF.tail(): returns the last 5 rows of a Pandas' DataFrame.
'''
def basic_operations():
    print('Calling head() on DataFrame:', '\n', DF.head(), '\n')
    print('Checking object type:', '\n', type(DF), '\n')
    print('Checking object shape:', '\n', DF.shape, '\n')
    print('Calling dtypes on DataFrame:', '\n', DF.dtypes, '\n')
    print('Calling info() on DataFrame:', '\n', DF.info(), '\n')
    print('Calling tail() on DataFrame:', '\n', DF.tail(), '\n')

'''
    Now, let's explore some more interesting operations and try to split our dataset in some different ways.
    
        * DF['country'][:5]: returns 5 rows of the columns named 'country'.
        * DF[['country', 'continent', 'year']]: returns a subset containing only the given 3 columns.
        * DF.ix[:, [0, -1]]: returns a subset containing only the first and last columns.
            - ix is used here because it will look at columns indexes or names (if the former is not found).
              Usually, DF.loc is used for columns names and DF.iloc for column indexes. However, when not found,
              an error is thrown. So, to keep it safe, better to use DF.ix.
        * DF.ix[:, list(range5)]: returns all the rows from columns 0 to 4.
        * DF.ix[:, list(0, 5, 2]: returns all the rows from every other column until 5 (excl.)
            - It returns columns 0, 2, 4.
        * DF.ix[[0, 99, 999]]: returns rows 0, 99 and 999 from all columns.
        * DF.ix[42, 'country']: returns the country on row 42.
    
'''
def split_operations():
    print('Printing the first 5 rows of the "country" column:', '\n', DF['country'][:5], '\n')

    country_DF = DF['country']
    print('Printing the head of the "country column:', '\n', country_DF.head(), '\n')
    print('Printing all countries:', '\n', DF.country, '\n')

    subset = DF[['country', 'continent', 'year']]
    print('Printing the head of the subset:', '\n', subset.head(), '\n')

    subset = DF.ix[:, [0, -1]]
    print('Printing the head of the subset:', '\n', subset.head(), '\n')

    sl = list(range(5))
    subset = DF.ix[:, sl]
    print('Printing the head of the subset:', '\n', subset.head(), '\n')

    ol = list(range(0, 5, 2))
    subset = DF.ix[:, ol]
    print('Printing the head of the subset:', '\n', subset.head(), '\n')

    subset = DF.ix[[0, 99, 999]]
    print('Printing the head of the subset:', '\n', subset, '\n')

    subset = DF.ix[42, 'country']
    print('Printing the head of the subset:', '\n', subset, '\n')

    subset = DF.ix[[0, 99, 999], ['country', 'lifeExp', 'gdpPercap']]
    print('Printing the head of the subset:', '\n', subset, '\n')

if __name__ == '__main__':
    basic_operations()
    split_operations()