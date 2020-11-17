# A script with code blocks relating to data cleaning

df = df.replace({'%': ''}, regex=True)
df[['col_1', 'col_2', 'col_3',]] = df[['col_1', 'col_2', 'col_3',]].apply(pd.to_numeric)


