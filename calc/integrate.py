from math import sqrt, isfinite


def ratio(x):
    return x / (x + 1)


def root(x):
    return sqrt(x * x + 1)


FUNCTIONS = {
    "ratio": (ratio, 0, 20, "x / (x + 1)"),
    "root": (root, -5, 5, "sqrt(x^2 + 1)"),
}

def calculate_integral(func, start, end, steps):
    """Вычисляет интеграл методом средних прямоугольников."""
    if not isinstance(steps, int) or not 1 <= steps <= 100000:
        raise ValueError("Количество шагов должно быть от 1 до 100000")

    if not isfinite(start) or not isfinite(end):
        raise ValueError("Границы интегрирования должны быть конечными числами")

    if end <= start:
        raise ValueError("Конец промежутка должен быть больше начала")

    width = (end - start) / steps
    total = 0.0

    for i in range(steps):
        x = start + (i + 0.5) * width
        total += func(x) * width

    return total

def integrate(func_name, start, end, steps):
    """Проверяет параметры и вычисляет определённый интеграл."""
    if func_name not in FUNCTIONS:
        raise ValueError("Неизвестная функция интегрирования")

    func, min_x, max_x, formula = FUNCTIONS[func_name]

    if start < min_x or end > max_x:
        raise ValueError(
            f"Для функции {func_name} границы должны быть "
            f"в диапазоне от {min_x} до {max_x}"
        )

    result = calculate_integral(func, start, end, steps)

    return formula, result
