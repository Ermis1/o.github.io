from pandas import *
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Series
series = pd.Series([2, 3, 4], ['a', 'b', 'c'])

print(series)
print(len(series))
print(type(series))
print(series['a'])
print(series.iloc[0])

series.name = 'Theseries'
print(series)

print(list(series))
print(dict(series))

series2 = pd.Series([3, 4, 5], ['a', 'b', 'c'])
print(series+series2)

series3 = pd.Series([66], ['d'])
print(series.append(series3))

print(series2.sort_index())
print(series2.sort_values())
print(series2.head(1))
print(series2.tail(1))
print(series2.count())

def m_func(m):
    return m + 9
print(series2.apply(m_func))

series2.pop('c')
print(series2)

plt.style.use('dark_background')
series.plot.bar()
plt.show()

series.to_csv('data.csv')

# dataframes

data = {
    'p':[1, 2, 3],
    'name':['Bob', 'Mark', 'John'],
    'age':[19, 22, 21]}

df = pd.DataFrame(data)
df.set_index('p', inplace=True)

print(df)
print(len(df))
print(type(df))
print(df.name)
print(df['name'])
print(df.iloc[0])
print(df['name'].iloc[0])
print(df.size)
print(df.ndim)
print(df.shape)
print(df.dtypes)
print(df.T)
print(df.count())
print(df['name'].count())
print(df.head(1))
print(df.tail(1))
print(df.describe())
print(df['age'].describe())
print(df.sum())
print(df['age'].sum())
print(df['age'].min())
print(df['age'].max())
print(df['age'].mean())
print(df['age'].median())
print(df['age'].std())
print(df['age'].prod())
print(df['age'].mode())

print(df['age'].apply(np.sqrt))
print(df['age'].apply(lambda x: x + 33))

df.plot.bar()
plt.show()

df.plot.hist()
plt.show()

names = {
    'p1':[1, 2],
    'name':['Ermis', 'Aris']}

ages = {
    'p1':[1, 2],
    'age':[13, 12]}

df1 = pd.DataFrame(names)
df2 = pd.DataFrame(ages)

df3 = pd.merge(df1, df2, on='p1', how='outer')
df3.set_index('p1', inplace=True)
print(df3)

for i in df:
    print(i)

for i in df['name']:
    print(i)

for i in df:
    if i=='name':continue # break
    print(i)

for i, e in df['age'].iteritems():
    print('{}, {}'.format(i, e))

for i in df.iterrows():
    print(i)

df3.sort_index(inplace=True)
print(df3)

df3.sort_values(by=['name', 'age'], inplace=True)
print(df3)

df3.to_csv('data1.csv')

df4 = pd.read_csv('data1.csv')
df4.set_index('p1', inplace=True)
print(df4)

print(df4.loc[(df4['age']==13)])