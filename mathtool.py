import sys

if len(sys.argv) == 1 or sys.argv[1] == '--help':
    print('mathtool — решение уравнений вида A*x^2 + B*x + C = 0', file=sys.stderr)
    print(' ', file=sys.stderr)
    print('Использование:', file=sys.stderr)
    print('    ','python mathtool.py                         вывод справки', file=sys.stderr)
    print('    ','python mathtool.py --help                  вывод справки', file=sys.stderr)
    print('    ','python mathtool.py solve                   ввод коэффициентов с клавиатуры', file=sys.stderr)
    print('    ','python mathtool.py solve -a 1 -b -3 -c 2   решение с заданными коэффициентами', file=sys.stderr)
    print(' ', file=sys.stderr)
    print('Коэффициенты A, B, C — целые числа, по модулю не превышающие 10000.', file=sys.stderr)
    sys.exit(0)

if sys.argv[1] == 'solve' and len(sys.argv) == 2:
    a = input("Введите A: ")
    b = input("Введите B: ")
    c = input("Введите C: ")
elif sys.argv[1] != 'solve':
    print("Неизвестная команда", file=sys.stderr)
    sys.exit(1)
elif sys.argv[1] == 'solve' and len(sys.argv) == 8:
    if sys.argv[2]!='-a' and sys.argv[4]!='-b' and sys.argv[6]!='-c':
        print("Неизвестная команда", file=sys.stderr)
        sys.exit(1)
    a = sys.argv[3]
    b = sys.argv[5]
    c = sys.argv[7]
if len(sys.argv)>8:
    print("Неверный набор параметров", file=sys.stderr)
    sys.exit(1)



try:
    a = int(a)
    b = int(b)
    c = int(c)
except ValueError:
    print("ОШИБКА: Коэффициент не является целым числом", file=sys.stderr)
    sys.exit(1)



from math import *

if abs(a)>10000 or abs(b)>10000 or abs(c)>10000:
    print("ОШИБКА: Значение вне допустимого диапазона", file=sys.stderr)
    sys.exit(1)
else:
    if a == 0 and b == 0:
        print("ОШИБКА: Введенные коэффициенты не образуют уравнение", file=sys.stderr)
        sys.exit(1)
    elif a == 0 and b!=0:
        print("Уравнение линейное")
        x = -c/b
        print(f"x = {x:.3f}")
    else:
        print("Уравнение квадратное")
        D = b**2 - 4*a*c
        print("Дискриминант:",D)
        if D>0:
            x1 = (-b + sqrt(D))/(2*a)
            x2 = (-b - sqrt(D))/(2*a)
            print(f"x1 = {x1:.3f}",f"x2 = {x2:.3f}")
        elif D==0:
            x = -b/(2*a)
            print(f"x = {x:.3f}")
        else:
            print("Действительных корней нет")