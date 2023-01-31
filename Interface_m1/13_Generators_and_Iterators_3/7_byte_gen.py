"""
Генератор продолжает существовать до явного закрытия или уничтожения.
Поэтому можно воспользоваться им для создания задачи с долгим сроком жизни. Пример генератора,
который получает байтовые фрагменты и собирает из них строки:
"""


def func():
    data = bytearray()
    line = None
    linecount = 0
    while True:
        part = yield line
        linecount += part.count(b'\n')
        data.extend(part)
        if linecount > 0:
            index = data.index(b'\n')
            line = bytes(data[:index + 1])
            data = data[index + 1:]
            linecount -= 1
        else:
            line = None


r = func()
print(r.send(None))
print(r.send(b'hello'))
print(r.send(b'world\nit '))
print(r.send(b'works!'))
print(r.send(b'\n'))

"""
Здесь генератор получает байтовые фрагменты, которые собираются в байтовый массив. 
Если массив содержит символ новой строки, строка извлекается и возвращается. В противном случае возвращается None.
"""