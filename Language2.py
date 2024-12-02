# -*- coding: utf-8 -*-

from konlpy.tag import Okt
from wordcloud import WordCloud
import collections
import matplotlib.pyplot as plt
okt = Okt()
text = '저 허름한 폐가에서도 사랑이 있었겠지 폐허가 된다 해도 나는 너를 너를 너를 이제는 읽을 수가 없는 옛 글자들처럼 발음을 잃어 버린대도 \        나는 너를 너를 서기가 영원해도 난 마지막 나야 시간이 버릴 때까지 난 너로 가득 흐를거야 소멸해 버릴 진실은 거짓말인 걸까 시간은 나 \        역시 부숴 버리겠지 결국 어차피 사라져 버린다면 아무도 믿지 않을 거짓말쟁이가 된대도 나는 너를 너를 서기가 영원해도 난 마지막 나야 \        시간이 버릴 때까지 난 난 나라는 시대의 처음과 끝이야 난 나라는 인류의 기원과 종말이야 넌 나라는 마음의 유일한 무덤이야 넌 나라는 \        시계의 마지막 시침이야 난 나라는 우주의 빅뱅과 블랙홀이야 난 나라는 신화의 실체와 허구야 난 너의 이름을 닮은 집을 지을거야 폐허가 \        된대도 나는 너를 너를 서기가 영원해도 넌 마지막 나야 시간이 버릴 때까지 난너로 가득 흐를거야'
sentence_tag = okt.pos(text)

adj_list = []
for word, tag in sentence_tag:
    if tag in ['Noun', 'Adjective']:(
        adj_list.append(word))

counts = collections.Counter(adj_list)
tag = counts.most_common(50)

print(tag)

font_path = 'C:/Windows/Fonts/malgun.ttf'
wc = WordCloud(font_path=font_path, background_color='white', max_font_size=60)
cloud = wc.generate_from_frequencies(dict(tag))

plt.imshow(cloud)
plt.show()