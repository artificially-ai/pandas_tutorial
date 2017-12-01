"""
    Organisation: ekholabs
    Author: wilder.rodrigues@ekholabs.ai
"""

from utils import dataset as ds

person = ds.load_survey('survey_person.csv')
site = ds.load_survey('survey_site.csv')
survey = ds.load_survey('survey_survey.csv')
visited = ds.load_survey('survey_visited.csv')


def merge_o2o():
    visited_subset = visited.ix[[0, 2, 6]] # take 3 rows of the dataframe
    print('Visited subset:', '\n', visited_subset, '\n')
    print('Site dataframe:', '\n', site, '\n')

    # We merge into 'site'; the 'left_on' has the column name of the datafram where we are going to merge;
    # the 'right_on' has the column name of the dataframe where we are merging from.
    o2o_merge = site.merge(visited_subset, left_on='name', right_on='site')
    print('Merged one-2-one dataset:', '\n', o2o_merge, '\n')


def merge_o2m():
    print('Visited dataframe:', '\n', visited, '\n')
    print('Site dataframe:', '\n', site, '\n')

    # We merge into 'site'; the 'left_on' has the column name of the datafram where we are going to merge;
    # the 'right_on' has the column name of the dataframe where we are merging from.
    o2o_merge = site.merge(visited, left_on='name', right_on='site')
    print('Merged one-2-one dataset:', '\n', o2o_merge, '\n')


def merge_m2m():
    # We first create 2 new datasets out of a merge to reproduce repeated entries.
    ps = person.merge(survey, left_on='ident', right_on='person')
    vs = visited.merge(survey, left_on='ident', right_on='taken')

    print('1-2-1 merge between Person and Survey:', '\n', ps, '\n')
    print('1-2-1 merge between Visited and Survey:', '\n', vs, '\n')

    # Many-2-many merge on the same column. Notice that following:
    '''
    vs dataframe has:
         ident   site       dated  taken person quant  reading
    0     619   DR-1  1927-02-08    619   dyer   rad     9.82
    1     619   DR-1  1927-02-08    619   dyer   sal     0.13
    
    vs_v (merged) dataframe has:
        ident_x   site     dated_x  taken person quant  reading  ident_y 
    0       619   DR-1  1927-02-08    619   dyer   rad     9.82      619
    1       619   DR-1  1927-02-08    619   dyer   rad     9.82      622
    2       619   DR-1  1927-02-08    619   dyer   rad     9.82      844
    3       619   DR-1  1927-02-08    619   dyer   sal     0.13      619
    4       619   DR-1  1927-02-08    619   dyer   sal     0.13      622
    5       619   DR-1  1927-02-08    619   dyer   sal     0.13      844
    
    The 'ident' column is common to both dataframes. Hence, it gets suffixes 'x' (for the left dataframe - vs)
    and 'y' (for the right dataframe - vs_v)
    
    Check here for more info: https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.merge.html
    '''
    vs_v = vs.merge(visited, on='site')
    print('Merged dataframe:', '\n', vs_v, '\n')


if __name__ == '__main__':
    merge_m2m()