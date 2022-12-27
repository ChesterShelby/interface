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


class Bus(Transport):
    def __init__(self, speed, color, seeds):
        super().__init__(speed, color)
        self.seeds = seeds

    def say_seeds(self):
        print(f'Кол-во мест {self.seeds}')


car1 = Car(100, 'yellow', 'Василий')
print(car1.color)
print(car1.speed)
print(car1.owner)
car1.beep()
car1.say_owner()
print()
bus1 = Bus(60, 'green', 33)
bus1.say_seeds()
