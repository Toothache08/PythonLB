import argparse
from calc.series import FORMULAS


def create_parser():
    """Создаёт разборщик аргументов приложения mathtool."""

    parser = argparse.ArgumentParser(
        prog="mathtool",
        description=(
            "mathtool — консольная программа для математических вычислений.\n\n"
            "Программа поддерживает четыре команды:\n"
            "  solve      — решение линейных и квадратных уравнений;\n"
            "  stats      — вычисление статистических показателей;\n"
            "  series     — вычисление суммы числового ряда;\n"
            "  integrate  — численное интегрирование функций.\n\n"
            "Для получения подробной информации о команде используйте:\n"
            "  python mathtool.py ИМЯ_КОМАНДЫ --help"
        ),
        epilog=(
            "Примеры:\n"
            "  python mathtool.py solve -a 1 -b -3 -c 2\n"
            "  python mathtool.py stats --input numbers.txt\n"
            "  python mathtool.py series --func sqplus --terms 100\n"
            "  python mathtool.py series --func third --eps 0.0001\n"
            "  python mathtool.py integrate --func root "
            "--from -5 --to 5 --steps 100\n\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        allow_abbrev=False,
    )

    commands = parser.add_subparsers(dest="command")

    # Решение уравнения
    solve_parser = commands.add_parser(
        "solve",
        help="решение линейных и квадратных уравнений",
        description=(
            "Решает уравнение вида A*x^2 + B*x + C = 0.\n\n"
            "Если A равно нулю, программа решает линейное уравнение.\n"
            "Если A не равно нулю, вычисляется дискриминант:\n"
            "D = B^2 - 4*A*C.\n\n"
            "Коэффициенты должны быть целыми числами.\n"
            "Допустимый диапазон каждого коэффициента: от -10000 до 10000."
        ),
        epilog=(
            "Примеры:\n"
            "  python mathtool.py solve -a 1 -b -3 -c 2\n"
            "  python mathtool.py solve -a 1 -b 2 -c 1\n"
            "  python mathtool.py solve -a 0 -b 2 -c -6\n\n"
            "Если коэффициенты не указаны, программа запросит их отдельно."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        allow_abbrev=False,
    )

    # Статистика
    stats_parser = commands.add_parser(
        "stats",
        help="показатели числовой последовательности",
        description=(
            "Вычисляет статистические характеристики набора чисел.\n\n"
            "Вычисляемые показатели:\n"
            "  количество чисел;\n"
            "  сумма и среднее арифметическое;\n"
            "  сумма квадратов и среднее квадратичное;\n"
            "  дисперсия;\n"
            "  среднее квадратичное отклонение;\n"
            "  выборочное стандартное отклонение;\n"
            "  минимальное и максимальное значения;\n"
            "  количество положительных и отрицательных чисел.\n\n"
            "Числа разделяются пробелами или переводами строк.\n"
            "Данные можно передать через файл или стандартный ввод."
        ),
        epilog=(
            "Примеры:\n"
            "  python mathtool.py stats --input numbers.txt\n"
            "  type numbers.txt | python mathtool.py stats\n\n"
            "Если в последовательности только одно число, "
            "выборочное стандартное отклонение не определено."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        allow_abbrev=False,
    )
    # Сумма ряда
    series_parser = commands.add_parser(
        "series",
        help="сумма числового ряда",
        description=(
            "Вычисляет сумму одного из доступных числовых рядов.\n\n"
            "Поддерживаются два ряда:\n"
            "  sqplus — чередующийся ряд со знаменателем n^2 + 1;\n"
            "  third  — чередующийся ряд со знаменателем 3*n.\n\n"
            "Способ вычисления задаётся одним из параметров:\n"
            "  --terms — количество слагаемых;\n"
            "  --eps   — ограничение на величину очередного слагаемого.\n\n"
            "Эти параметры нельзя использовать одновременно."
        ),
        epilog=(
            "Примеры:\n"
            "  python mathtool.py series --func sqplus --terms 100\n"
            "  python mathtool.py series --func third --terms 50\n"
            "  python mathtool.py series --func sqplus --eps 0.0001\n"
            "  python mathtool.py series --func third --eps 0.0001\n\n"
            "Максимальное количество слагаемых при задании --terms: 10000.\n"
            "Максимальное количество итераций: 100000."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        allow_abbrev=False,
    )
    # Численное интегрирование
    integrate_parser = commands.add_parser(
        "integrate",
        help="численное интегрирование",
        description=(
            "Вычисляет определённый интеграл численным методом "
            "средних прямоугольников.\n\n"
            "Доступные функции:\n"
            "  ratio — x / (x + 1), допустимый промежуток [0; 20];\n"
            "  root  — sqrt(x^2 + 1), допустимый промежуток [-5; 5].\n\n"
            "Параметры:\n"
            "  --from  — начало промежутка интегрирования;\n"
            "  --to    — конец промежутка интегрирования;\n"
            "  --steps — количество шагов разбиения."
        ),
        epilog=(
            "Примеры:\n"
            "  python mathtool.py integrate --func ratio "
            "--from 0 --to 20 --steps 1000\n"
            "  python mathtool.py integrate --func root "
            "--from -5 --to 5 --steps 1000\n\n"
            "Количество шагов должно быть от 1 до 100000.\n"
            "Конец промежутка должен быть больше начала."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        allow_abbrev=False,
    )
    return parser