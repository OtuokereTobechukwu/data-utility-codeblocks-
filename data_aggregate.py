# A small script to aggregate data

agg_func = {'col_1': ['sum'], 'col_2': ['nunique']}
df.groupby(['col3']).agg(agg_func).style.format('{0:0f}')
