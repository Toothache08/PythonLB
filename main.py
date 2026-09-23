import sys

A = input()
if A == '--help' or A == '':
    print('mathtool — решение уравнений вида A*x^2 + B*x + C = 0')
    print(' ')
    print('Использование:')
    print('    ','python mathtool.py                         вывод справки')
    print('    ','python mathtool.py --help                  вывод справки')
    print('    ','python mathtool.py solve                   ввод коэффициентов с клавиатуры')
    print('    ','python mathtool.py solve -a 1 -b -3 -c 2   решение с заданными коэффициентами')
    print(' ')
    print('Коэффициенты A, B, C — целые числа, по модулю не превышающие 10000.')
    sys.exit(0)
elif A != 'solve':
    print("Неизвестная команда", file=sys.stderr)
    sys.exit(1)
elif A == 'solve':
    a = input("Введите A: ")
    b = input("Введите B: ")
    c = input("Введите C: ")

if a == '' or b == '' or c == '':
    print('mathtool — решение уравнений вида A*x^2 + B*x + C = 0')
    print(' ')
    print('Использование:')
    print('    ','python mathtool.py                         вывод справки')
    print('    ','python mathtool.py --help                  вывод справки')
    print('    ','python mathtool.py solve                   ввод коэффициентов с клавиатуры')
    print('    ','python mathtool.py solve -a 1 -b -3 -c 2   решение с заданными коэффициентами')
    print(' ')
    print('Коэффициенты A, B, C — целые числа, по модулю не превышающие 10000.')
    sys.exit(0)



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



