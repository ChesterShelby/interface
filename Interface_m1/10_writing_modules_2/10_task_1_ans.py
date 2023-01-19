def func(n):
    n1 = n
    n2 = int(str(n) * 2)
    n3 = int(str(n) * 3)
    print(n1, n2, n3)
    return n1 + n2 + n3


print(func(int(input())))

