"""
    Organisation: ekholabs
    Author: wilder.rodrigues@ekholabs.ai
"""

import numpy as np
import pandas as pd


def create_dataset(index):
    A = np.random.randn(5, 4) * 5

    dict = {'A' : A[:, 0],
            'B' : A[:, 1],
            'C' : A[:, 2],
            'D': A[:, 3]}
    dataframe = pd.DataFrame(dict)
    dataframe.to_csv('dataset_' + str(index) + ".csv", index=False)


def concatdatasets_rows():
    ds1 = pd.read_csv('dataset_1.csv')
    ds2 = pd.read_csv('dataset_2.csv')
    ds3 = pd.read_csv('dataset_3.csv')

    rows_stitched = pd.concat([ds1, ds2, ds3], ignore_index=True)
    print(rows_stitched)


def append_datasets_rows():
    ds1 = pd.read_csv('dataset_1.csv')
    ds2 = pd.read_csv('dataset_2.csv')
    ds3 = pd.read_csv('dataset_3.csv')

    rows_stitched = ds1.append(ds2).append(ds3, ignore_index=True)
    print(rows_stitched)


def append_dictionary_rows():
    ds1 = pd.read_csv('dataset_1.csv')
    data_dict = {'A' : np.random.randn(), 'B' : np.random.randn(), 'C' : np.random.randn(), 'D' : np.random.randn()}

    rows_stitched = ds1.append(data_dict, ignore_index=True)
    print(rows_stitched)


def concat_datasets_cols():
    # Concatenating multiple datasets has complications with indexing if column names are the same.
    ds1 = pd.read_csv('dataset_1.csv')
    ds2 = pd.read_csv('dataset_2.csv')
    ds3 = pd.read_csv('dataset_3.csv')

    cols_stitched = pd.concat([ds1, ds2, ds3], axis=1)
    print(cols_stitched)


def append_datasets_cols():
    ds1 = pd.read_csv('dataset_1.csv')
    ds1['E'] = [np.random.randn(), np.random.randn(), np.random.randn(), np.random.randn(), np.random.randn()]
    print(ds1)


def append_datasets_series():
    ds1 = pd.read_csv('dataset_1.csv')
    ds1['E'] = pd.Series([np.random.randn(), np.random.randn(), np.random.randn(), np.random.randn(), np.random.randn()])
    print(ds1)


def append_datasets_cols_ignore_index():
    #Ignoring the index will reset the column names.
    ds1 = pd.read_csv('dataset_1.csv')
    ds2 = pd.read_csv('dataset_2.csv')
    ds3 = pd.read_csv('dataset_3.csv')

    cols_stitched = pd.concat([ds1, ds2, ds3], axis=1, ignore_index=True)
    print(cols_stitched)


def concat_rows_reindexed_columns():
    ds1 = pd.read_csv('dataset_1.csv')
    ds2 = pd.read_csv('dataset_2.csv')
    ds3 = pd.read_csv('dataset_3.csv')

    # Rename the columns, keeping some overlapping between ds1 and ds3
    ds1.columns = ['A', 'B', 'C', 'D']
    ds2.columns = ['E', 'F', 'G', 'H']
    ds3.columns = ['A', 'C', 'F', 'I']

    rows_stitched = pd.concat([ds1, ds2, ds3])

    # Observe the NaN value which are created due to colliding column names.
    print(rows_stitched)

    # Use join='inner' to show which indexes ar common. It also allows to create a DataFrame with only aligned columns
    rows_stitched = pd.concat([ds1, ds2, ds3], join='inner')
    print(rows_stitched)

    rows_stitched = pd.concat([ds1, ds3], join='inner')
    print(rows_stitched)


def concat_cols_reindexed_rows():
    ds1 = pd.read_csv('dataset_1.csv')
    ds2 = pd.read_csv('dataset_2.csv')
    ds3 = pd.read_csv('dataset_3.csv')

    # Rename the columns, keeping some overlapping between ds1 and ds3
    ds1.index = [0, 1, 2, 3, 4]
    ds2.index = [5, 6, 7, 8, 9]
    ds3.index = [0, 1, 6, 10, 11]

    cols_stitched = pd.concat([ds1, ds2, ds3], axis=1)

    # Observe the NaN value which are created due to colliding column names.
    print(cols_stitched)

    # Use join='inner' to show which indexes ar common. It also allows to create a DataFrame with only aligned columns
    cols_stitched = pd.concat([ds1, ds2, ds3], axis=1, join='inner')
    print(cols_stitched)

    cols_stitched = pd.concat([ds1, ds3], axis=1, join='inner')
    print(cols_stitched)


if __name__ == '__main__':
    # create_dataset(index=1)
    # create_dataset(index=2)
    # create_dataset(index=3)
    concat_cols_reindexed_rows()
