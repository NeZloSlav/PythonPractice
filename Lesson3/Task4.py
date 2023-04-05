# Заданы две клетки шахматной доски. Если они покрашены в один цвет, то выведите слово YES, а
# если в разные цвета — то NO. Программа получает на вход четыре числа от 1 до 8 каждое,
# задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.

try:
    row1 = int(input('Введите строку 1-ой клетки: '))
    column1 = int(input('Введите столбец 1-ой клетки: '))

    row2 = int(input('Введите строку 2-ой клетки: '))
    column2 = int(input('Введите строку 2-ой клетки: '))

    if row1 % 2 == 0 and column1 % 2 == 0 and row2 % 2 == 0 and column2 % 2 == 0:
        print("YES")
    elif row1 % 2 == 0 and column1 % 2 == 1 and row2 % 2 == 0 and column2 % 2 == 0:
        print('YES')
    elif row1 % 2 == 1 and column1 % 2 == 1 and row2 % 2 == 1 and column2 % 2 == 1:
        print('YES')
    elif row1 % 2 == 1 and column1 % 2 == 0 and row2 % 2 == 1 and column2 % 2 == 0:
        print('YES')
    elif row1 % 2 == 1 and column1 % 2 == 1 and row2 % 2 == 0 and column2 % 2 == 0:
        print('YES')
    elif row1 % 2 == 0 and column1 % 2 == 0 and row2 % 2 == 1 and column2 % 2 == 1:
        print('YES')
    else:
        print('NO')
except:
    print('Вы ввели некорректное значение')