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


car1 = Car(100, 'yellow', 'Василий')
print(car1.color)
print(car1.speed)
print(car1.owner)
car1.beep()
car1.say_owner()


