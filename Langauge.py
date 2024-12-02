from konlpy.tag import Okt
okt = Okt()
token = okt.morphs('폐허가 된다 할지라도')
print(token)