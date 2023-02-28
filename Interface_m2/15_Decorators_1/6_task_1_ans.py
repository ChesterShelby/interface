def decor(func):
    def wrapper():
        print('Начало функции')
        func()
        print('Конец функции')

    return wrapper


@decor
def func():
    print('Привет мир!')


func()
