"""
    Organisation: ekholabs
    Author: wilder.rodrigues@ekholabs.ai
"""

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
anscombe = sns.load_dataset('anscombe')


def histogram(kde=False, rug=True, histogram=True):
    hist = sns.distplot(tips['total_bill'], kde=kde, rug=rug, hist=histogram)
    hist.set_title('Total Bill Histogram with Density Plot')
    plt.show()


def plot_count_column(column='day'):
    count_plot = sns.countplot(column, data=tips)
    count_plot.set_title('Count of Days')
    count_plot.set_xlabel('Day of the Week')
    count_plot.set_ylabel('Frequency')
    plt.show()


def plot_scatter_reg(x='total_bill', y='tip'):
    scatter = sns.regplot(x=x, y=y, data=tips)
    scatter.set_title('Scatter Reg Plot of Total Bill and Tip')
    plt.show()


def plot_scatter_lm(x='total_bill', y='tip'):
    scatter = sns.lmplot(x=x, y=y, data=tips)
    scatter.fig.suptitle('Scatter Lm Plot of Total Bill and Tip')
    plt.show()


def plot_joint(x='total_bill', y='tip', kind='hex'): # trye using kind='kde'
    scatter = sns.jointplot(x=x, y=y, data=tips, kind=kind)
    scatter.set_axis_labels(xlabel='Total Bill', ylabel='Tip')
    scatter.fig.suptitle('Scatter Joint Plot of Total Bill and Tip')
    plt.show()


def plot_kde_density():
    count_plot = sns.kdeplot(data=tips['total_bill'], data2=tips['tip'], shade=True)
    count_plot.set_title('Kernel Density Plot of Total Bill and Tip')
    count_plot.set_xlabel('Total Bill')
    count_plot.set_ylabel('Tip')
    plt.show()


def plot_bar():
    bar = sns.barplot(x='time', y='total_bill', data=tips)
    bar.set_title('Bar Plot of Average Total Bill per Time of Day')
    bar.set_xlabel('Timeof day')
    bar.set_ylabel('Average total bill')
    plt.show()


def plot_box():
    box = sns.boxplot(x='time', y='total_bill', data=tips)
    box.set_title('Box Plot of Total Bill per Time of Day')
    box.set_xlabel('Timeof day')
    box.set_ylabel('Total bill')
    plt.show()


def plot_violin():
    violin = sns.violinplot(x='time', y='total_bill', data=tips)
    violin.set_title('Violin Plot of Total Bill per Time of Day')
    violin.set_xlabel('Timeof day')
    violin.set_ylabel('Total bill')
    plt.show()


def plot_grid():
    subset_tips = tips[['total_bill', 'tip', 'size']]
    grid = sns.PairGrid(subset_tips)
    grid = grid.map_upper(sns.regplot)
    grid = grid.map_lower(sns.kdeplot)
    grid = grid.map_diag(sns.distplot, rug=True)
    plt.show()


def plot_violin_split():
    violin = sns.violinplot(x='time', y='total_bill', hue='sex', data=tips, split=True)
    violin.set_title('Violin Plot of Total Bill per Time of Day')
    violin.set_xlabel('Timeof day')
    violin.set_ylabel('Total bill')
    plt.show()


def plot_scatter_lm_split(x='total_bill', y='tip'):
    scatter = sns.lmplot(x=x, y=y, data=tips, hue='sex', fit_reg=False)
    scatter.fig.suptitle('Scatter Lm Plot of Total Bill and Tip')
    plt.show()


def plot_custom_scatter_lm(x='total_bill', y='tip'):
    scatter = sns.lmplot(x=x, y=y, data=tips, hue='sex', fit_reg=False, markers=['o', 'x'], scatter_kws={'s' : tips['size'] * 10}, col='day')
    scatter.fig.suptitle('Scatter Lm Plot of Total Bill and Tip')
    plt.show()


def plot_anscombe_lm():
    scatter = sns.lmplot(x='x', y='y', data=anscombe, col='dataset', col_wrap=2, fit_reg=False)
    scatter.fig.suptitle('Facets of the Anscombe dataset') # check the implementation in basic_plot.py
    plt.show()


def plot_pairs():
    sns.pairplot(tips, hue='sex')
    plt.show()


def plot_facet_time():
    facet = sns.FacetGrid(data=tips, col='time')
    facet.map(sns.distplot, 'total_bill', rug=True)
    plt.show()


def plot_facet_day():
    facet = sns.FacetGrid(data=tips, col='day', hue='sex')
    facet = facet.map(plt.scatter, 'total_bill', 'tip')
    facet.add_legend()
    plt.show()


def plot_custom_scatter_facet(x='total_bill', y='tip'):
    scatter = sns.lmplot(x=x, y=y, data=tips, hue='sex', fit_reg=False, markers=['o', 'x'], scatter_kws={'s' : tips['size'] * 10}, col='day')
    scatter.fig.suptitle('Scatter Lm Plot of Total Bill and Tip')
    plt.show()


def plot_facet_smoker():
    facet = sns.FacetGrid(data=tips, col='time', row='smoker', hue='sex')
    facet = facet.map(plt.scatter, 'total_bill', 'tip')
    facet.add_legend()
    plt.show()


def plot_custom_factor(x='day', y='total_bill'):
    sns.factorplot(x=x, y=y, data=tips, hue='sex', col='time', row='smoker', kind='violin')
    plt.show()


if __name__ == '__main__':
    plot_custom_factor()