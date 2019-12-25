# Pandas

```python
import numpy as np
import pandas as pd

s = pd.Series([1, 3, 6, np.nan, 44, 1])
dates = pd.date_range('20190606', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20191108'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3]*4, dtype='int32'),
                    'E': pd.Categorical(['test', 'train', 'test', 'train']),
                    'F': 'foo'})
# 属性
print(df2.dtypes)
print(df2.index)
print(df2.columns)
print(df2.values)
print(df2.describe())
print(df2.T)
df2.sort_index(axis=1, ascending=False)
df2.sort_values(by='E')

# 数据选取
dates = pd.date_range('20191108', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
print(df['A'], '\n', df.A)
print(df[0:3], '\n', df['20191109':'20191111'])

# select by label: loc
print(df.loc['20191110'])
print(df.loc[:, ['A', 'B']])

# select by position: iloc
print(df.iloc[3:, :2])

# Boolean indexing
print(df[df.B > 8])
df.A[df.A > 4] = 0

# 处理缺失数据 NaN
df.dropna(axis=0, how='any')  # how={'any', 'all'}
df.fillna(value=0)
df.isnull()
np.any(df.isnull()) == True

# 导入导出数据
data = pd.read_csv
data.to_csv('data.csv')
data.to_pickle('data.pkl')

# concatenating
df1 = pd.DataFrame(np.ones((3, 4))*0, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4))*1, columns=['a', 'b', 'c', 'd'], dtype=np.int32)
df3 = pd.DataFrame(np.ones((3, 4))*1, columns=['a', 'b', 'c', 'd'], dtype=np.float)
res = pd.concat([df1, df2, df3], axis=0, ignore_index=True)

# join, ['inner', 'outer']
df1 = pd.DataFrame(np.ones((3, 4))*0, index=[1, 2, 3], columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4))*1, index=[2, 3, 4], columns=['b', 'c', 'd', 'e'])
res = pd.concat([df1, df2], join='inner', ignore_index=True)
res = pd.concat([df1, df2], axis=1, join_axes=[df1.index])  # join_axes

s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'e'])
res = df1.append(s1, ignore_index=True)  # append
res = df1.append([df1, df2], ignore_index=True)

# merge by key
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})
res = pd.merge(left, right, on='key')

# 包含不同的keys
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})
res = pd.merge(left, right, on=['key1', 'key2']) # how='inner'
"""
  key1 key2   A   B   C   D
0   K0   K0  A0  B0  C0  D0
1   K1   K0  A2  B2  C1  D1
2   K1   K0  A2  B2  C2  D2
"""
res = pd.merge(left, right, how='outer', on=['key1', 'key2'], indicator=True)
# indicator='indicator_column'
"""
  key1 key2    A    B    C    D      _merge
0   K0   K0   A0   B0   C0   D0        both
1   K0   K1   A1   B1  NaN  NaN   left_only
2   K1   K0   A2   B2   C1   D1        both
3   K1   K0   A2   B2   C2   D2        both
4   K2   K1   A3   B3  NaN  NaN   left_only
5   K2   K0  NaN  NaN   C3   D3  right_only
"""
# merge by index
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                    index=['K0', 'K1', 'K2'])
right = pd.DataFrame({'C': ['C0', 'C1', 'C2'],
                      'D': ['D0', 'D1', 'D2']},
                     index=['K1', 'K2', 'K3'])
res = pd.merge(left, right, how='inner', left_index=True, right_index=True)
"""
     A   B   C   D
K1  A1  B1  C0  D0
K2  A2  B2  C1  D1
"""
res = pd.merge(left, right, how='outer', left_index=True, right_index=True)
"""
      A    B    C    D
K0   A0   B0  NaN  NaN
K1   A1   B1   C0   D0
K2   A2   B2   C1   D1
K3  NaN  NaN   C2   D2
"""
# 重复数据
boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})
res = pd.merge(boys, girls, on='k', how='inner', suffixes=['_boy', '_girl'])
"""
    k  age_boy  age_girl
0  K0        1         4
1  K0        1         5
"""

# matplotlib.pyplot
import matplotlib.pyplot as plt
data = pd.Series(np.random.randn(1000), index=np.arange(1000))
data = data.cumsum()
data.plot()
plt.show()

data = pd.DataFrame(np.random.randn(1000, 4),
                    index=np.arange(1000),
                    columns=list("ABCD"))
# print(data.head())
data = data.cumsum()
data.plot()
plt.show()

# plot methods
# 'bar', 'hist', 'box', 'kde', 'area', 'scatter', 'hexbin', 'pie'
ax = data.plot.scatter(x='A', y='B', color='DarkBlue', label='Class 1')
data.plot.scatter(x='A', y='C', color='DarkGreen', label='Class 2', ax=ax)
plt.show()
```

