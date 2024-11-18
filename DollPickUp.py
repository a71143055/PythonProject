from Doll import Doll
import random as rand

class DollPickUp:
    Dolls = {
        1 : Doll("피까츄", "수컷", 5000, "medium"),
        2 : Doll("바비인형", "여성", 7500, "tall"),
        3 : Doll("카봇저글링", "수컷", 6400, "small")
    }

    def pickUp(self,num : int):
        if rand.randint(100) <= 30:
            print(f'{self.Dolls[num].name}을(를) 뽑았습니다.')
            self.Dolls[num].info()

    def dolls(self):
        for i, v in enumerate(self.Dolls):
            doll = self.Dolls[v]
            print(f'{i}. 이름 : {doll.name} | 성별 : {doll.gender} | 가격 : {doll.price}원 | 사이즈 : {doll.size}')