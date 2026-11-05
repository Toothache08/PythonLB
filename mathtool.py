import sys
import math

from cli import create_parser
from calc.equation import solve
from calc.stats import calculate_stats
from calc.series import calculate_series, FORMULAS
from calc.integrate import integrate


def handle_solve(args):
    values = (args.a, args.b, args.c)

    if all(value is None for value in values):
        try:
            a = input("Введите A: ")
            b = input("Введите B: ")
            c = input("Введите C: ")
        except EOFError:
            raise ValueError("Не удалось прочитать коэффициенты")
    elif any(value is None for value in values):
        raise ValueError("Нужно указать все три коэффициента: -a, -b, -c")
    else:
        a, b, c = values

    try:
        a, b, c = int(a), int(b), int(c)
    except ValueError:
        raise ValueError("Коэффициент не является целым числом")

    kind, d, roots = solve(a, b, c)

    if kind == "линейное":
        print("Уравнение линейное")
        print(f"x = {roots[0]:.3f}")
        return 0

    print("Уравнение квадратное")
    print("Дискриминант:", d)

    if len(roots) == 2:
        print(f"x1 = {roots[0]:.3f}", f"x2 = {roots[1]:.3f}")
    elif len(roots) == 1:
        print(f"x = {roots[0]:.3f}")
    else:
        print("Действительных корней нет")

    return 0


def handle_stats(args):
    try:
        if args.input:
            with open(args.input, "r", encoding="utf-8-sig") as file:
                source = file
                numbers = []

                for line in source:
                    for word in line.split():
                        try:
                            value = float(word)
                        except ValueError:
                            raise ValueError(
                                f"{word} не является числом"
                            )

                        if not math.isfinite(value):
                            raise ValueError(
                                f"{word} не является конечным числом"
                            )

                        if abs(value) > 10000:
                            raise ValueError(
                                f"Значение {word} вне допустимого диапазона "
                                "[-10000; 10000]"
                            )

                        numbers.append(value)

                        if len(numbers) > 20:
                            raise ValueError(
                                "Количество чисел не должно превышать 20"
                            )
        else:
            numbers = []

            for line in sys.stdin:
                for word in line.split():
                    try:
                        value = float(word)
                    except ValueError:
                        raise ValueError(
                            f"{word} не является числом"
                        )

                    if not math.isfinite(value):
                        raise ValueError(
                            f"{word} не является конечным числом"
                        )

                    if abs(value) > 10000:
                        raise ValueError(
                            f"Значение {word} вне допустимого диапазона "
                            "[-10000; 10000]"
                        )

                    numbers.append(value)

                    if len(numbers) > 20:
                        raise ValueError(
                            "Количество чисел не должно превышать 20"
                        )

    except OSError as error:
        raise ValueError(
            f"Не удалось прочитать файл: {error}"
        ) from error

    if not numbers:
        raise ValueError("Числовой ряд пуст")

    result = calculate_stats(numbers)

    print("Количество:", result["count"])
    print(f'Сумма: {result["sum"]:.3f}')
    print(f'Ср. арифм.: {result["mean"]:.3f}')
    print(f'Сумма кв.: {result["sum_squares"]:.3f}')
    print(f'Ср. кв.: {result["rms"]:.3f}')
    print(f'Дисперсия: {result["variance"]:.3f}')
    print(f'СКО: {result["std_dev"]:.3f}')

    if result["sample_std_dev"] is None:
        print("Станд. откл.: не определено")
    else:
        print(f'Станд. откл.: {result["sample_std_dev"]:.3f}')

    print(f'Наименьшее: {result["min"]:.3f}')
    print(f'Наибольшее: {result["max"]:.3f}')
    print("Положительных:", result["positive_count"])
    print("Отрицательных:", result["negative_count"])

    return 0

def handle_series(args):
    term_function, formula = FORMULAS[args.func]

    total, count = calculate_series(
        term_function,
        terms=args.terms,
        eps=args.eps,
    )

    print("Функция:", args.func)
    print("Формула:", formula)
    print("Количество слагаемых:", count)
    print(f"Сумма: {total:.4f}")

    return 0

def handle_integrate(args):
    formula, result = integrate(
        args.func,
        args.start,
        args.end,
        args.steps,
    )

    print("Функция:", args.func)
    print("Формула:", formula)
    print(f"Интеграл: {result:.6f}")

    return 0


def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return 0

    try:
        if args.command == "solve":
            return handle_solve(args)
        if args.command == "stats":
            return handle_stats(args)
        if args.command == "series":
            return handle_series(args)
        if args.command == "integrate":
            return handle_integrate(args)
    except ValueError as error:
        print(f"ОШИБКА: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())