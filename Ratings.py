from konlpy.tag import Okt
import collections
import matplotlib.pyplot as plt
from wordcloud import wordcloud
import pandas as pd

df = pd.read_table('./data/ratings.txt')
print(df)