"""
Исходя из данного примера сделаем небольшой вывод: Если экземпляр obj поддерживает перебор,
он предоставляет метод obj.__iter__(), возвращающий итератор. Итератор iter реализует один метод iter.__next__(),
который возвращает следующий объект или выдает исключение StopIteration для обозначения конца перебора.
Эти методы используются реализацией команды for и другими операциями, которые неявно выполняют перебор.
"""


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)
for x in myiter:
    print(x)
