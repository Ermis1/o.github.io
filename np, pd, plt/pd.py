from pandas import *
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Series
series = pd.Series([1, 2, 3], ['a', 'b', 'c'])
print(series)
print(len(series))
print(type(series))
print(series.iloc[0])
print(series['a'])

series.name = 'Theseries'
print(series)

print(list(series))
print(dict(series))

series2 = pd.Series([4, 5, 6], ['a', 'b', 'c'])
print(series+series2)

series3 = pd.Series([33], ['d'])
print(series.append(series3))

series4 = pd.Series([22, 1, 4], ['k', 'z', 'e'])

print(series4.sort_index())
print(series4.sort_values())
print(series4.count())
print(series4.head(1))
print(series4.tail(1))

def m_func(m):
    return m + 3

print(series4.apply(m_func))

series4.pop('e')
print(series4)

series4.plot.bar()
plt.show()

series.to_csv('Theseries.csv')

# dataframes
data = {
    'p':[1, 2, 3],
    'name':['Ermis', 'Aris', 'Bob'],
    'age':[13, 12, 16]
}

df = pd.DataFrame(data)
print(df)

df.set_index('p', inplace=True)
print(df)

print(len(df))
print(type(df))
print(df.name)
print(df['name'])
print(df.iloc[0])
print(df['name'].iloc[0])
print(df.size)
print(df.shape)
print(df.ndim)
print(df.dtypes)
print(df.T)
print(df.head(1))
print(df.tail(1))
print(df.count())
print(df.describe())
print(df['age'].describe())
print(df['name'].count())
print(df.sum())
print(df['age'].sum())
print(df['age'].min())
print(df['age'].max())
print(df['age'].median())
print(df['age'].mean())
print(df['age'].std())
print(df['age'].mode())
print(df['age'].prod())

print(df['age'].apply(np.sqrt))
print(df['age'].apply(lambda x: x*3))

df.plot.bar()
plt.show()

df.plot.hist()
plt.show()

names = {
    'p1':[1, 2, 3],
    'name':['john', 'Mark', 'Justin']
}

ages = {
    'p1':[1, 2, 3],
    'age':[19, 20, 23]
}

df2 = pd.DataFrame(names)
df3 = pd.DataFrame(ages)

df4 = pd.merge(df2, df3, on='p1', how='outer')
print(df4)
df4.set_index('p1', inplace=True)
print(df4)

for i in df:
    print(i)

for i in df['age']:
    print(i)

for i in df:
    if 'name'==i: continue # we can also say 'break'
    print(i)

for i, e in df['age'].iteritems():
    print('{}, {}'.format(i, e))

for i in df.iterrows():
    print(i)

df4.sort_index(inplace=True)
print(df4)

df4.sort_values(by=['name', 'age'], inplace=True)
print(df4)

df4.to_csv('data.csv')

df5 = pd.read_csv('data.csv', delimiter=',')
df5.set_index('p1', inplace=True)
print(df5)