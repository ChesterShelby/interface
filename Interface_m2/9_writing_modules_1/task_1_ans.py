def add(num1: float, num2: float) -> float:
    return num1 + num2


def sub(num1: float, num2: float) -> float:
    return num1 - num2


def mul(num1: float, num2: float) -> float:
    return num1 * num2


def div(num1: float, num2: float) -> str | float:
    if num2 == 0:
        return 'Деление на 0'
    return num1 / num2