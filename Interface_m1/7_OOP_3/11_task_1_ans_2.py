#   travka - обозначает плотоядное животное или травоядное
#   homea - домашнее животное или дикое

class Animal:
    def __init__(self, name, color, travka, homea="Домашнее"):
        self._color = color
        self._travka = travka
        self.homea = homea
        self.name = name
        self.__walk()

    def __walk(self):
        print(f'{self.name} идет куда-то...')

    @property
    def statistic(self):
        return f'Это животное {self._color} цвета, оно {self._travka} и {self.homea}'



Animal1 = Animal("Барсик", "Разного", 'плотоядное')
print(Animal1.homea)
# Animal1._Animal__walk()
a = Animal1.statistic
print(a)
