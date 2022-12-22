with open('2.txt') as file:
   str1 = file.read()

word_list = str1.split()
result = ', '.join(word_list)
print(result)
