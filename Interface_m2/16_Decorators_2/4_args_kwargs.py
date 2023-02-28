"""
Можно использовать *args и **kwargs и для функции wrapper, если сигнатура заранее неизвестна,
или будут приниматься разные типы функций.

args и kwargs используются, когда мы не знаем заранее сколько аргументов передаст пользователь.
args - обычные аргументы, переданные через запятую, а kwargs - именованные аргументы.
"""


def func(*args, **kwargs):
    print(f'{args=}')
    print(f'{kwargs=}')


func(1, 2, 3, a=5, b=1)