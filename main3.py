import numpy as np
import pandas as pd

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