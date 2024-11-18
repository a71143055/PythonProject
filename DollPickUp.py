from Doll import Doll
import random as rand

class DollPickUp:
    Dolls = {
        Doll("피까츄", "수컷", 5000, "medium"),
        Doll("바비인형", "여성", 7500, "tall"),
        Doll("카봇저글링", "수컷", 6400, "small")
    }

    def pickUp(self,num):
        if rand.randint(100) <= 30:
