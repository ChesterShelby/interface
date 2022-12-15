file = open('example_1.txt', 'a')     # в данном случае нам подойдет параметр 'a', так как 'w' полностью перезапишет файл
file.write('\npython')
file.close()
file = open('example_1.txt', 'r')
print(file.read())
file.close()
