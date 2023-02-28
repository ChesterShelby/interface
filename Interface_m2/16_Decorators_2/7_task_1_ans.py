def get_type(func):
    def wrapper(*args, **kwargs):
        print('Вызываем функцию')
        result = func(*args, **kwargs)
        print(result)
        print(f'Тип данных, возвращаемых функцией {type(result)}')

    return wrapper


@get_type
def func(a, b):
    return a + b


func(4, b=5)
