import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

english_scores = np.array(df['english'])
math_scores = np.array(df['mathematics'])

poly_fit = np.polyfit(english_scores, math_scores, 1)
poly_1d = np.poly1d(poly_fit)
xs = np.linspace(english_scores.min(), english_scores.max())
ys = poly_1d(xs)

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)
c = ax.hist2d(english_scores, math_scores, bins=[9,8], range=[(35,80),(55,95)])

# ax.plot(xs,ys,color='gray', label=f'{poly_fit[1]:.2f}+{poly_fit[0]:.2f}x')

ax.set_xlabel('english')
ax.set_ylabel('mathematics')
ax.set_xticks(c[1])
ax.set_yticks(c[2])

# ax.legend(loc='upper left')

fig.colorbar(c[3], ax=ax)
plt.show()

anscombe_data = np.load('./data/ch3_anscombe.npy')
print(anscombe_data.shape)
print(anscombe_data[0])

fig,axes = plt.subplots(nrows=2,ncols=2,figsize=(10,10),
                        sharex=True, sharey=True)

xs = np.linspace(0,30,100)
for i, data in enumerate(anscombe_data):
    poly_fit=np.polyfit(data[:,0],data[:,1], 1)
    poly_1d = np.poly1d(poly_fit)
    ys = poly_1d(xs)

    ax = axes[i//2,i%2]
    ax.set_xlim([4,20])
    ax.set_ylim([3,13])
    ax.set_title(f'data{i+1}')
    ax.scatter(data[:,0], data[:,1])
    ax.plot(xs,ys,color='gray')

    plt.tight_layout()
    plt.show()