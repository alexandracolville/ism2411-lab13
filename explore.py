import pandas as pd

# Exercise 1
df = pd.read_csv('data/retail_sales.csv')
print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

# Exercise 2
south = df[df['region'] == 'South']
print(len(south))
print(south.head())

# Exercise 3
top = df.sort_values('revenue', ascending=False).head(5)
print(top)

# Exercise 4
big_south = df[(df['region'] == 'South') & (df['revenue'] > 1000)]
print(len(big_south))
print(big_south.head())
