with open('2.txt') as file:
   str1 = file.read()

word_list = str1.split()
result = ''
for word in word_list:
   result += word + ', '
print(result)
print(*word_list)
