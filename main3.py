import numpy as np
import pandas as pd

pd.options.display.max_columns = None
pd.options.display.max_rows = None

df = pd.read_csv('./data/ch2_scores_em.csv',
                 index_col='student number')

en_scores = np.array(df['english'])[:10]
ma_scores = np.array(df['mathematics'])[:10]

scores_df = pd.DataFrame({'english' : en_scores,
                          'mathematics' : ma_scores},
                         index = pd.Index(['A','B','C','D','E',
                                           'F','G','H','I','J'],
                                          name = 'student'))

print(scores_df)

summary_df = scores_df.copy()
summary_df['english_deviation'] = summary_df['english'] - summary_df['english'].mean()
summary_df['mathematics_deviation'] = summary_df['mathematics'] - summary_df['mathematics'].mean()
summary_df['product of deviations'] = summary_df['english_deviation'] * summary_df['mathematics_deviation']

print(summary_df)
print(summary_df['product of deviations'].mean())

cov_mat = np.cov(en_scores, ma_scores, ddof=0)
print(cov_mat)
print(cov_mat[0,1], cov_mat[1,0])

np.cov(en_scores, ma_scores, ddof=0)[0,1] / (np.std(en_scores) * np.std(ma_scores))
np.corrcoef(en_scores, ma_scores)
print(scores_df.corr())