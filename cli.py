import argparse
from calc.series import FORMULAS

def create_parser():
    """Создаёт разборщик аргументов приложения mathtool."""
    parser = argparse.ArgumentParser(
        description="mathtool — математические вычисления",
        allow_abbrev=False,
    )

    commands = parser.add_subparsers(dest="command")

    # Решение уравнения
    solve_parser = commands.add_parser(
        "solve", help="решение линейных и квадратных уравнений",
        allow_abbrev=False,
    )
    solve_parser.add_argument("-a", help="коэффициент A")
    solve_parser.add_argument("-b", help="коэффициент B")
    solve_parser.add_argument("-c", help="коэффициент C")

    # Статистика
    stats_parser = commands.add_parser(
        "stats", help="показатели числовой последовательности",
        allow_abbrev=False,
    )
    stats_parser.add_argument(
        "--input", help="файл с числами",
    )

    # Сумма ряда
    series_parser = commands.add_parser(
        "series", help="сумма числового ряда",
        allow_abbrev=False,
    )
    series_parser.add_argument(
    "--func",
    required=True,
    choices=sorted(FORMULAS),
    help="имя ряда",
    )
    group = series_parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--terms", type=int, help="число слагаемых")
    group.add_argument("--eps", type=float, help="требуемая точность")

    # Численное интегрирование
    integrate_parser = commands.add_parser(
        "integrate", help="численное интегрирование",
        allow_abbrev=False,
    )
    integrate_parser.add_argument("--func", required=True, help="имя функции")
    integrate_parser.add_argument("--from", dest="start", type=float, required=True,
                                  help="начало промежутка")
    integrate_parser.add_argument("--to", dest="end", type=float, required=True,
                                  help="конец промежутка")
    integrate_parser.add_argument("--steps", type=int, required=True,
                                  help="число шагов")

    return parser