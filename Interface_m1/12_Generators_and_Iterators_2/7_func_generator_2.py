def func(num):
    while num > 0:
        yield num
        num -= 1


result = func(5)
print(result)

print(next(result))
print(next(result))
print(next(result))

"""
При вызове next() функция-генератор выполняет команды до достижения yield. Команда yield возвращает результат, 
после чего выполнение функции приостанавливается до следующего вызова next(). 
При возобновлении выполнение продолжается с команды, следующей за yield.
"""
