def third_term(n):
    """Возвращает n-е слагаемое первого ряда."""
    sign = 1 if n % 2 == 1 else -1
    return sign / (3 * n)


def sqplus_term(n):
    """Возвращает n-е слагаемое второго ряда."""
    sign = 1 if n % 2 == 1 else -1
    return sign / (n * n + 1)


FORMULAS = {
    "third": (third_term, "1/(3*n)"),
    "sqplus": (sqplus_term, "1/(n*n + 1)"),
}

MAX_TERMS = 10000
MAX_EPS = 0.0001
MAX_ITERATIONS = 100000


def calculate_series(func, terms=None, eps=None):
    """Вычисляет сумму ряда по количеству слагаемых или точности."""
    if terms is None and eps is None:
        raise ValueError("Нужно указать количество слагаемых или точность")

    if terms is not None:
        if not isinstance(terms, int) or not 1 <= terms <= MAX_TERMS:
            raise ValueError(
                f"Количество слагаемых должно быть от 1 до {MAX_TERMS}"
            )

    if eps is not None:
        if not 0 < eps <= MAX_EPS:
            raise ValueError(
                f"Точность должна быть больше 0 и не превышать {MAX_EPS}"
            )

    total = 0.0
    count = 0

    while True:
        count += 1
        total += func(count)

        if terms is not None and count >= terms:
            break

        if eps is not None and abs(func(count)) < eps:
            break

        if count >= MAX_ITERATIONS:
            raise ValueError("Превышено максимальное число итераций")

    return total, count

