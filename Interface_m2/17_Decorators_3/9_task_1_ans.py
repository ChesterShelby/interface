find_num = 10001
simpleNum = 3
count = 1
result = 0
while count < find_num:
    for x in range(3, int(simpleNum ** 0.5) + 1, 2):
        if simpleNum % x == 0:
            break
    else:
        result = simpleNum
        count += 1
    simpleNum += 2
print(result)
