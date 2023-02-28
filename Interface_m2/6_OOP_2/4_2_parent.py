class Transport:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color

    def beep(self):
        print('beep')


class Car(Transport):
    def __init__(self, speed, color, owner):
        super().__init__(speed, color)
        self.owner = owner

    def say_owner(self):
        print(f'Владелец {self.owner}')


class SportCar(Car, Transport):
    pass


car1 = SportCar(speed=100, color='yellow', owner='Иван')
car1.beep()
car1.say_owner()
