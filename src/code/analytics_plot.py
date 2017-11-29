"""
    Organisation: ekholabs
    Author: wilder.rodrigues@ekholabs.ai
"""

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')


def histogram():
    fig = plt.figure()
    axis1 = fig.add_subplot(1, 1, 1)
    axis1.hist(tips['total_bill'], bins=10) # bins = number of bars on the histogra.
    axis1.set_title('Histogram of Total Bill')
    axis1.set_xlabel('Total Bill')
    axis1.set_ylabel('Frquency')

    plt.show()


def scattered():
    scatter_plot = plt.figure()
    axis1 = scatter_plot.add_subplot(1, 1, 1)
    axis1.scatter(tips['total_bill'], tips['tip'])
    axis1.set_title('Scatterplot of Total Bill vs Tip')
    axis1.set_xlabel('Total Bill')
    axis1.set_ylabel('Tip')

    plt.show()


def box():
    boxplot = plt.figure()
    axis1 = boxplot.add_subplot(1, 1, 1)
    axis1.boxplot([tips[tips['sex'] == 'Female']['tip'], tips[tips['sex'] == 'Male']['tip']], labels=['Female', 'Male'])
    axis1.set_title('Boxplot of Tips by Sex')
    axis1.set_xlabel('Sex')
    axis1.set_ylabel('Tip')

    plt.show()


def scattered_encoded(factor = 10, alpha_blending = 0.5):
    tips['encoded_sex'] = tips['sex'].apply(lambda sex: int(sex == 'Female'))
    scatter_plot = plt.figure()
    axis1 = scatter_plot.add_subplot(1, 1, 1)
    axis1.scatter(tips['total_bill'], tips['tip'], s=tips['size'] * factor, c=tips['encoded_sex'], alpha=alpha_blending)
    axis1.set_title('Scatterplot of Total Bill vs Tip')
    axis1.set_xlabel('Total Bill')
    axis1.set_ylabel('Tip')

    plt.show()


if __name__ == '__main__':
    scattered_encoded()