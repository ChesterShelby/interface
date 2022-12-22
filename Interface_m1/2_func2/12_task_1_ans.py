def get_year(n):
    if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
        return 'Високосный'
    else:
        return 'Обычный'


year = int(input('Введите год: '))
print(get_year(year))


gett_year = lambda x: 'Високосный' if (x % 4 == 0 and x % 100 != 0) or x % 400 == 0 else 'Обычный'
print(gett_year(year))
