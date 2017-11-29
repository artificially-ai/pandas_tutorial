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


if __name__ == '__main__':
    create_dataset(index=1)
    create_dataset(index=2)
    create_dataset(index=3)