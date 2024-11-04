import numpy as np
import pandas as pd

df = pd.read_csv('./data/ch2_scores_em.csv', index_col = 'student number')
print(df)
print(type(df))

scores = np.array(df['english'])[:10]
print(scores)
print(type(scores))
print(scores.shape)

scores_df = pd.DataFrame({'score' : scores}, index = pd.Index([chr(i) for i in range(ord('A'), ord('A') + 10)], name = 'student'))
test = np.array(scores_df)[:10]
test = np.reshape(test, newshape=(-1,2))

print(test)
print(test.shape)

z = (scores - np.mean(scores)) / np.std(scores)
print(z)

print(np.mean(z), np.std(z, ddof=0))

z = 50 + 10 * (scores - np.mean(scores)) / np.std(scores)
print(z)

scores_df['deviation value'] = z
print(scores_df)

english_scores = np.array(df['english'])
print(pd.Series(english_scores).describe())

freq,_ = np.histogram(english_scores, bins = 10, range=(0,100))
print(freq)

freq_class = [f' {i}~{i+10}' for i in range(0, 100, 10)]
freq_dist_df = pd.DataFrame({'frequency' : freq},
                            index = pd.Index(freq_class,
                                             name = 'class'))

print(freq_dist_df)

class_value = [(i+(i+10))//2 for i in range(0,100,10)]
print(class_value)

rel_freq = freq / freq.sum()
print(rel_freq)

cum_rel_freq = np.cumsum(rel_freq)
print(cum_rel_freq)

freq_dist_df['class value'] = class_value
freq_dist_df['relative frequency'] = rel_freq
freq_dist_df['cumulative relative frequency'] = cum_rel_freq
freq_dist_df = freq_dist_df[['class value', 'frequency','relative frequency', 'cumulative relative frequency']]

print(freq_dist_df)