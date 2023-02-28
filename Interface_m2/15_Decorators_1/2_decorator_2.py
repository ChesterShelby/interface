def decorator(func):
    '''Основная функция'''
    print('декоратор')

    def wrapper():
        print('-- до функции', func.__name__)
        func()
        print('-- после функции', func.__name__)

    return wrapper


@decorator
def wrapped():
    print('--- обернутая функция')


print('- старт программы...')
wrapped()
print('- конец программы')
