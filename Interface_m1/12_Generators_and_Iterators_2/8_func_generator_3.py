def func(num):
    while num > 0:
        yield num
        num -= 1


result = func(5)
print(result.__next__())
print(result.__next__())
print(result.__next__())
