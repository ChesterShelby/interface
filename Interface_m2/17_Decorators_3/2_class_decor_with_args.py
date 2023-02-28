class DecoratorArgs:
    def __init__(self, name):
        print('> Декоратор с аргументами ＿init＿:', name)
        self.name = name

    def __call__(self, func):
        def wrapper(a, b):
            print(">>> до обернутой функции")
            func(a, b)
            print('>>> после обернутой функции')

        return wrapper


@DecoratorArgs("test")
def add(a, b):
    print('функция add:', a, b)


print(">> старт")
add(10, 20)
print('>> конец')
