def func(num):
    while num > 0:
        yield num
        num -= 1


for num in func(5):
    print(num)

# или например
a = sum(func(5))
print(a)
