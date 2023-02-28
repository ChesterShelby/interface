"""
Функция next() - возвращает следующий элемент итератора, вызвав его метод __next__().
Синтаксис:
next(iterator, default)

    iterator - объект итератора
    default - значение по умолчанию, которое будет возвращено вместо исключения StopIteration.


Если все значение перебраны:

    возбуждается исключение StopIteration, если значение по умолчанию default не задано
    возвращается значение default, если оно задано

"""

numbers = [1, 2, 3, 4]
result = (x * x for x in numbers)

print(next(result))
print(next(result))


