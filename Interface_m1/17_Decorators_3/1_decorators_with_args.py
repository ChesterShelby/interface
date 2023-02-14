def decorator_with_args(name):
    print('> decorator_with_args:', name)

    def real_decorator(func):
        print('>> сам декоратор', func.__name__)

        def decorated(*args, **kwargs):
            print('>>> перед функцие', func.__name__)
            ret = func(*args, **kwargs)
            print('>>> после функции', func.__name__)
            return ret

        return decorated

    return real_decorator


@decorator_with_args('test')
def add(a, b):
    print('>>>> функция add')
    return a + b


print("старт программы")
r = add(10, 10)
print(r)
print('конец программы')
