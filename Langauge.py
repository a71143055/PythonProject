from konlpy.tag import Okt
okt = Okt()
token = okt.morphs('폐허가 된다 해도')
print(token)