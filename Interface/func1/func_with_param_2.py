def draw_box(height, width):    # функция принимает два параметра
    for i in range(height):
        print('*' * width)


k = int(input('Сколько раз?'))


for i in range(k):
    h = int(input('Enter height: '))
    w = int(input('Enter width: '))
    draw_box(h, w)
    print()
