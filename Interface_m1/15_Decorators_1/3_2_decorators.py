def decorator_1(func):
    print('декоратор 1')

    def wrapper():
        print("перед функцией 2")
        # print('перед функцией')
        func()

    return wrapper


def decorator_2(func):
    print('декоратор 2')

    def wrapper():
        print('перед функцией')
        func()

    return wrapper


@decorator_1
@decorator_2
def basic_1():
    print('basic_1')


@decorator_1
def basic_2():
    print('basic_2')


print('>> старт')
basic_1()
basic_2()
print('>> конец')
