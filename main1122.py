import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

d = pd.DataFrame({
    'date' : ['2019-01-03', '2021-11-22', '2023-01-05'],
    'name' : ['J','Y','O'],
    'value' : ['123','456','789']
})

t1 = pd.to_datetime(d.date, format='%Y-%m-%d')
t2 = pd.to_numeric(d.value)
print(t1)
print(t2)

df = pd.DataFrame(
    np.random.randn(8,3),
    columns = ['C1','C2','C3'])
df.loc[2,'C2'] = np.nan
df.loc[3,'C2'] = np.nan
print(df)
df = df.fillna(0)
print(df)

df = pd.DataFrame(
    np.random.randn(8,3),
    columns = ['C1','C2','C3'])
df.loc[2,'C2'] = np.nan
df.loc[3,'C2'] = np.nan
print(df)
df = df.fillna(df.mean())
print(df)

df = pd.DataFrame(
    np.random.randn(8,3),
    columns = ['C1','C2','C3'])
df['location'] = ['서울','서울','경기','인천','강원','경기','서울','경기']
df.loc[2,'C2'] = np.nan
df.loc[3,'C2'] = np.nan
print(df)
df3 = df['location'].fillna(df['location'].mode()[0])
print(df3)

df = pd.DataFrame(
    np.random.randn(8,3),
    columns = ['C1','C2','C3'])
df.loc[2,'C2'] = np.nan
df.loc[3,'C2'] = np.nan
print(df)
df = df.dropna()
print(df)

a = ['A','B','A','C','C','A','B','A','D','D','A','D']
a = pd.Series(a)
a_dict = {'A':1,'B':2,'C':3,'D':4}
b = a.map(a_dict)
p = pd.DataFrame({'변환 전' : a, '변환 후' : b})
print(p)

df = pd.DataFrame(
    np.random.randn(8,3),
    columns = ['C1','C2','C3'])
df.loc[2,'C2'] = 1
df.loc[3,'C2'] = -10

plt.boxplot([df['C1'],df['C3']])
plt.show()

df = pd.DataFrame(
    np.random.randn(8,3),
    columns = ['C1','C2','C3'])
df.loc[2,'C2'] = 1
df.loc[3,'C2'] = -10

sns.heatmap(df.corr(), annot=True)
plt.show()