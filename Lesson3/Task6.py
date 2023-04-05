# Шахматный король ходит по горизонтали, вертикали и диагонали, но только на 1 клетку. Даны
# две различные клетки шахматной доски, определите, может ли король попасть с первой клетки на
# вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, задающие
# номер столбца и номер строки сначала для первой клетки, потом для второй клетки. Программа
# должна вывести YES, если из первой клетки ходом короля можно попасть во вторую или NO в
# противном случае.

try:
    print('Введите строку 1-ой клетки: ')
    row1 = int(input())
    print('Введите столбец 1-ой клетки: ')
    column1 = int(input())

    print('Введите сроку 2-ой клетки: ')
    row2 = int(input())
    print('Введите столбец 2-ой клетки: ')
    column2 = int(input())

    if row1 + 1 == row2 and column1 == column2:
        print('YES')
    elif column1 + 1 == column2 and row1 == row2:
        print('YES')
    elif column1 + 1 == column2 and row1 + 1 == row2:
        print('YES')
    elif row1 - 1 == row2 and column1 == column2:
        print('YES')
    elif column1 - 1 == column2 and row1 == row2:
        print('YES')
    elif column1 - 1 == column2 and row1 - 1 == row2:
        print('YES')
    else:
        print('NO')

except:
    print('Вы ввели некорректное значение')