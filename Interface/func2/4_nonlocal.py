def a():
    x = 5

    def b():
        nonlocal x
        x += 1
        
    b()
    print(x)


a()
