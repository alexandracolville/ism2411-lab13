# 1. A boolean filter tests every row against a condition and returns True or False, keeping only the rows where the condition is True.
# 2. df["revenue"] returns a 1D pandas Series, while df[["revenue"]] returns a 2D pandas DataFrame. The distinction matters when adding columns or performing operations expecting specific data structures.
# 3. Pandas can effortlessly process millions of rows of data in seconds without crashing or slowing down like Excel often does.

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

# Exercise 5
df['per_unit'] = df['revenue'] / df['quantity']
print(df.head())
print(df['per_unit'].mean())

# Exercise 6
print(df['region'].unique())
print(df['region'].value_counts())

# Exercise 7
subset = df[['region', 'product', 'revenue']]
print(subset.shape)

# Exercise 8
df.to_csv('data/explored.csv', index=False)