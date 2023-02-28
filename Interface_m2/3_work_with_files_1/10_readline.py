x = open('example_1.txt','r')
print(x.readline())
print(x.readline())     # прочитать первую строку
print(x.readlines(2))  # прочитать вторую строку
print(x.readlines())  # прочитать все строки
