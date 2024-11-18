class Doll:
    def __init__(self, name, gender, price, size):
        self.name = name
        self.gender = gender
        self.price = price
        self.size = size
    def info(self):
        print(f'이름 : {self.name}')
        print(f'성별 : {self.gender}')
        print(f'가격 : {self.price}원')
        print(f'사이즈 : {self.size}')