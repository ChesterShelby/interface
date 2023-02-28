class MyClass:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1


obj = MyClass(5)
for i in obj.__iter__():
    print(i)
print()
print(next(obj.__iter__()))
print(next(obj.__iter__()))
print(next(obj.__iter__()))

"""при каждом переборе метод __iter__() создает новый генератор"""
