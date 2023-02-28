def func():
    while True:
        n = yield
        print(n)


"""
В примере выше функция выполняется бесконечно. Для закрытия генератора можно воспользоваться методом close():
"""

r = func()
r.send(None)
r.send(1)
r.close()
# r.send(2)
