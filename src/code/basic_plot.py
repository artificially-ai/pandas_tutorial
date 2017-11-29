"""
    Organisation: ekholabs
    Author: wilder.rodrigues@ekholabs.ai
"""

import seaborn as sns
import matplotlib.pyplot as plt

anscombe = sns.load_dataset('anscombe')


def plot_dataset_I():
    dataset_1 =  anscombe[anscombe.dataset == 'I']
    plt.plot(dataset_1.x, dataset_1.y, 'o') # 'o' is used to make matplotlib plot dots instead of lines.
    plt.show()


def plot_dataset_II():
    dataset_2 =  anscombe[anscombe.dataset == 'II']
    plt.plot(dataset_2.x, dataset_2.y, 'o')
    plt.show()

def plot_dataset_III():
    dataset_3 =  anscombe[anscombe.dataset == 'III']
    plt.plot(dataset_3.x, dataset_3.y, 'o')
    plt.show()


def plot_dataset_IV():
    dataset_4 =  anscombe[anscombe.dataset == 'IV']
    plt.plot(dataset_4.x, dataset_4.y, 'o')
    plt.show()


def plot_figure():
    dataset_1 = anscombe[anscombe.dataset == 'I']
    dataset_2 = anscombe[anscombe.dataset == 'II']
    dataset_3 = anscombe[anscombe.dataset == 'III']
    dataset_4 = anscombe[anscombe.dataset == 'IV']

    fig = plt.figure()

    axix1 = fig.add_subplot(2, 2, 1)
    axix2 = fig.add_subplot(2, 2, 2)
    axix3 = fig.add_subplot(2, 2, 3)
    axix4 = fig.add_subplot(2, 2, 4)

    axix1.plot(dataset_1.x, dataset_1.y, 'o')
    axix2.plot(dataset_2.x, dataset_2.y, 'o')
    axix3.plot(dataset_3.x, dataset_3.y, 'o')
    axix4.plot(dataset_4.x, dataset_4.y, 'o')

    axix1.set_title('dataset_1')
    axix2.set_title('dataset_2')
    axix3.set_title('dataset_3')
    axix4.set_title('dataset_4')

    fig.suptitle('Anscombe Dataset')
    plt.show()


if __name__ == '__main__':
    plot_figure()