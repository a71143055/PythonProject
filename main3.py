import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sympy.physics.control.control_plots import matplotlib

pd.options.display.max_columns = None
pd.options.display.max_rows = None

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

# freq_dist_df.loc[freq_dist_df['frequency'].idxmax(), 'class value']

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
freq, _, _ = ax.hist(english_scores, bins=10, range=(0,100), color = 'powderblue')
ax.set_xlabel('score')
ax.set_ylabel('personal number')
ax.set_xticks(np.linspace(0,100,10+1))
ax.set_yticks(np.arange(0,freq.max()+1))
plt.grid(True)
plt.show()

fig = plt.figure(figsize=(10,6))
ax1 = fig.add_subplot(111)
ax2 = ax1.twinx()
weights = np.ones_like(english_scores) / len(english_scores)
rel_freq, _, _ = ax1.hist(english_scores, bins=25, range=(0,100), weights = weights)

cum_rel_freq = np.cumsum(rel_freq)
class_value = [(i+(i+4))//2 for i in range(0, 100, 4)]

ax2.plot(class_value,cum_rel_freq,ls='--',marker='o', color = 'gray')

ax1.set_xlabel('score')
ax1.set_ylabel('relative frequency')
ax2.set_ylabel('calculative relative frequency')
ax1.set_xticks(np.linspace(0,100,25+1))
plt.show()

fig = plt.figure(figsize=(5,6))
ax = fig.add_subplot(111)
ax.boxplot(english_scores, labels=['english'])
plt.show()

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

x = range(0,100)
y = [v * v for v in x]

ax1.plot(x,y)
ax2.bar(x,y)

plt.show()