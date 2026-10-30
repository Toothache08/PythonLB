from math import *


mx = 10_000


def solve(a, b, c):
    for value in (a, b, c):
        if not isinstance(value, int):
            raise ValueError("Коэффициент должен быть целым числом")
        if abs(value) > mx:
            raise ValueError(f"Значение вне допустимого диапазона [{mx*-1};{mx}]")

    if a == 0 and b == 0:
        raise ValueError("Введенные коэффициенты не образуют уравнение")

    if a == 0:
        return "линейное", None, [-c / b]

    d = b**2 - 4 * a * c

    if d > 0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        korn = [x1, x2]
    elif d == 0:
        korn = [-b / (2 * a)]
    else:
        korn = []

    return "квадратное", d, korn