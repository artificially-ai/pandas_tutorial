"""
    Organisation: ekholabs
    Author: wilder.rodrigues@ekholabs.ai
"""

from utils import dataset as ds

person = ds.load_survey('survey_person.csv')
site = ds.load_survey('survey_site.csv')
survey = ds.load_survey('survey_survey.csv')
visited = ds.load_survey('survey_visited.csv')


def merge_visited():
    visited_subset = visited.ix[[0, 2, 6]] # take 3 rows of the dataframe
    print('Visited subset:', '\n', visited_subset, '\n')
    print('Site dataframe:', '\n', site, '\n')

    # We merge into 'site'; the 'left_on' has the column name of the datafram where we are going to merge;
    # the 'right_on' has the column name of the dataframe where we are merging from.
    o2o_merge = site.merge(visited_subset, left_on='name', right_on='site')
    print('Merged one-2-one dataset:', '\n', o2o_merge, '\n')


if __name__ == '__main__':
    merge_visited()