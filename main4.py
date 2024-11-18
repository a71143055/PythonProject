import pandas as pd
import numpy as np

raw_data = {'first_name' : ['Jason', np.nan, 'Tina', 'Jake', 'Amy'],
            'last_name' : ['Miller', np.nan, 'Ali', 'Milner', 'Cooze'],
            'age' : [42, np.nan,36,24,73],
            'sex' : ['m', np.nan, 'f', 'm', 'f'],
            'preTestScore' : [4, np.nan, np.nan, 2, 3],
            'postTestScore' : [25, np.nan, np.nan, 62, 70]}

df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'sex', 'preTestScore', 'postTestScore'])

print(df)
print(df.isnull().sum() / len(df))
print(df.dropna())
df_cleaned = df.dropna(how='all')
print(df_cleaned)
df['location'] = np.nan
print(df.dropna(axis=1, how='all'))
print(df.dropna(axis=0, thresh=1))
print(df.dropna(thresh=5))
print(df.fillna(0))
df["preTestScore"].fillna(df["preTestScore"].mean(), inplace=True)
print(df)
print(df.groupby("sex")["postTestScore"].transform("mean"))
df["postTestScore"].fillna(df.groupby("sex")["postTestScore"].transform("mean"), inplace=True)
print(df)
edges = pd.DataFrame({'source' : [0,1,2],
                     'target' : [2,2,3],
                     'weight' : [3,4,5],
                     'color' : ['red', 'blue', 'blue']})
print(edges)
print(edges.dtypes)
print(pd.get_dummies((edges)))
print(pd.get_dummies(edges["color"]))
print(pd.get_dummies(edges[["color"]]))