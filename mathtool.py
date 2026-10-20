import sys

mx = 7

if len(sys.argv) == 1 or sys.argv[1] == '--mathtool':
    print('mathtool — решение уравнений вида A*x^2 + B*x + C = 0')
    print(' ')
    print('Использование:')
    print('    ','python mathtool.py                         вывод справки')
    print('    ','python mathtool.py --help                  вывод справки')
    print('    ','python mathtool.py solve                   ввод коэффициентов с клавиатуры')
    print('    ','python mathtool.py solve -a 1 -b -3 -c 2   решение с заданными коэффициентами')
    print(' ')
    print(f'Коэффициенты A, B, C — целые числа, по модулю не превышающие {mx}.')
    sys.exit(0)



def test(n):
    try:
        n = int(n)
        return test2(n)
    except ValueError:
        print("ОШИБКА: Коэффициент не является целым числом", file=sys.stderr)
        sys.exit(1)

def test2(f):
    if abs(f)>mx:
        print("ОШИБКА: Значение вне допустимого диапазона", file=sys.stderr)
        sys.exit(1)
    return (int(f))



if sys.argv[1] == 'solve' and len(sys.argv) == 2:
    a = test(input("Введите A: "))
    b = test(input("Введите B: "))
    c = test(input("Введите C: "))
elif sys.argv[1] != 'solve':
    print("Неизвестная команда", file=sys.stderr)
    sys.exit(1)
elif sys.argv[1] == 'solve' and len(sys.argv) == 8:
    if sys.argv[2]!='-a' or sys.argv[4]!='-b' or sys.argv[6]!='-c':
        print("Неизвестная команда", file=sys.stderr)
        sys.exit(1)
    else:
        a = test(sys.argv[3])
        b = test(sys.argv[5])
        c = test(sys.argv[7])
else:
    print("Неверный набор параметров", file=sys.stderr)
    sys.exit(1)



from math import *

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