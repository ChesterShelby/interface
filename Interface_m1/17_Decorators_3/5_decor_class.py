"""
Декоратор можно использовать для декорирования класса. Отличие лишь в том, что
декоратор получает класс, а не функцию.
Singleton - это класс с одним экземпляром. Его можно сохранить как атрибут
функции-обертки и вернуть при запросе. Это полезно в тех случаях, когда, например,
ведется работа с соединением с базой данных.
"""


def singleton(cls):
    """Класс Singleton (один экземпляр)"""

    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance

    wrapper_singleton.instance = None
    return wrapper_singleton


@singleton
class TheOne:
    pass


print('старт')
first_one = TheOne()
second_one = TheOne()
print(id(first_one))
print(id(second_one))
print('конец')
