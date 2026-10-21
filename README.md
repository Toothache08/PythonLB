# mathtool — лабораторная работа № 2

Консольное приложение на Python для решения уравнений, расчёта статистики,
суммирования рядов и численного интегрирования.

## Запуск

```bash
python mathtool.py --help
python mathtool.py solve -a 1 -b -3 -c 2
python mathtool.py stats --input numbers.txt
python mathtool.py series --func sqplus --terms 6
python mathtool.py series --func sqplus --eps 0.0001
python mathtool.py integrate --func ratio --from 0 --to 20 --steps 1000
```

Если у `solve` не указаны коэффициенты, приложение запросит их с клавиатуры.
Если у `stats` не указан `--input`, числа читаются из стандартного ввода.

## Структура проекта

- `mathtool.py` — аргументы командной строки и вывод результата.
- `calc/equation.py` — решение уравнений.
- `calc/stats.py` — чтение чисел и статистические показатели.
- `calc/series.py` — суммы рядов.
- `calc/integration.py` — численное интегрирование.
- `numbers.txt` — пример входных данных.
- `tests.txt` — примеры проверок.

Ошибки входных данных возвращают код 1; ошибки аргументов командной строки,
обнаруженные `argparse`, возвращают код 2.
