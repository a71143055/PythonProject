import numpy as np
import pandas as pd

df = pd.read_csv('./data/ch2_scores_em.csv', index_col = 'student number')
# print(df.head())
scores = np.array(df['english'])[:10]
# print(scores)
scores_df = pd.DataFrame({'score' : scores}, index = pd.Index(['A','B','C','D','E','F','G','H','I','J'], name = 'student'))
# print(scores_df)

# print(sum(scores) / len(scores))
# print(np.mean(scores))
# print(scores_df.mean())

sorted_scores = np.sort(scores)
# print(sorted_scores)

n = len(sorted_scores)
if n % 2 == 0:
    m0 = sorted_scores[n//2 - 1]
    m1 = sorted_scores[n//2]
    median = (m0 + m1) / 2
else:
    median = sorted_scores[(n+1)//2 - 1]

# print(median)
# print(np.median(scores))
# print(scores_df.median())

series = pd.Series([1,1,1,2,2,3])
# print(series.mode())

series = pd.Series([1,2,3,4,5])
# print(series.mode())

print("표본 분산 : {}".format(np.var(series, ddof=0)))
print("불편 분산 : {}".format(np.var(series, ddof=1)))