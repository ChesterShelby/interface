simple = [3]
number = 3
count = 3
res = 0
while count <= 10001:
    number += 2
    simpleNuber = True
    for i in simple:
        if number < i ** 2:  # числа кратные i, начинают высчитывать с і (квадрат)
            break
        else:
            if number % i == 0:
                simpleNuber = False
                break
    if simpleNuber:
        simple.append(number)
        count += 1
print(res)
