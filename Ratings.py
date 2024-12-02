from konlpy.tag import Okt
import collections
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd

df = pd.read_table('./data/ratings.txt')

print(df['id'].nunique())
print(df.isnull().sum())

df = df.dropna(how='any')
print(df.isnull().sum())

df['document'] = df['document'].str.replace("[^ㄱ-ㅎ ㅏ-ㅣ 가-힣]","")
print(df)

okt = Okt()
adj_list = []
for sentence in df['document']:
    sentence_tag = okt.pos(sentence)
    for word, tag in sentence_tag:
        if tag in ['Noun', 'Adjective']:
            adj_list.append((word))
counts = collections.Counter(adj_list)
tag = counts.most_common(50)
print(tag)

font_path = 'C:/Windows/Fonts/malgun.ttf'
wc = WordCloud(font_path=font_path, background_color='white', max_font_size=60)
cloud = wc.generate_from_frequencies(dict(tag))
plt.imshow(cloud)
plt.show()