class Car:
    def __init__(self,Model="Genesis",Color="black"):
        self.Model = Model
        self.Color = Color
        self.speed = 0
    def speedIncrease(self, speed):
        self.speed += speed
        print(f'speed = {self.speed}')
    def speedDecrease(self, speed):
        self.speed -= speed
        print(f'speed = {self.speed}')
    def stop(self):
        self.speed = 0
        print(f'speed = {self.speed}')

class SportsCar(Car):
    def __init__(self):
        super().__init__()
        self.lid = 'closed'
    def openLid(self):
        self.lid = 'opened'
        print(f'{self.Color} Car {self.Model} lid is {self.lid}')
    def closeLid(self):
        self.lid = 'closed'
        print(f'{self.Color} Car {self.Model} lid is {self.lid}')

# myCar = Car()
# myCar.stop()
# myCar.Model = "Abante"
# myCar.speedIncrease(16)

CarList = [SportsCar(),SportsCar(),SportsCar()]

CarList[0].Model = "포르쉐"
CarList[1].Model = "람보르기니"
CarList[2].Model = "페라리"

for car in CarList:
    print(car.Model)