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
            print(f'{}')