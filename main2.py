import numpy as np
import pandas as pd

df = pd.read_csv('./data/ch2_scores_em.csv', index_col = 'student number')
print(df)
print(type(df))

scores = np.array(df['english'])[:10]
print(scores)
print(type(scores))
print(scores.shape)

scores_df = pd.DataFrame(data=scores)
test = np.array(scores_df)[:10]
test = np.reshape(test, newshape=(-1,2))

print(test)
print(test.shape)