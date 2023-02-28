from functools import wraps


def decorator(func):
    """Декоратор"""

    @wraps(func)
    def decorated():
        """функция Decorated"""
        func()

    return decorated


@decorator
def wrapped():
    """Оборачиваемая функция"""
    print('функция wrapped')


print("старт программы…")
print(wrapped.__name__)
print(wrapped.__doc__)
print('конец программы')
