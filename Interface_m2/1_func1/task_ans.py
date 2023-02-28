def func(side1, side2):
    area = side1 * side2
    perimetr = (side1 + side2) * 2
    print(area, perimetr)


func(int(input('enter side1: ')), int(input('enter side2: ')))
