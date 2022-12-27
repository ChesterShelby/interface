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

    def beep(self):
        print('Hello')


class SportCar(Car, Transport):
    pass


car1 = SportCar(100, 'yellow', 'Иван')
car1.beep()
car1.say_owner()

a = Transport(100, 'kek')
a.beep()