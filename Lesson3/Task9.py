# Шахматный конь ходит буквой “Г” — на две клетки по вертикали в любом направлении и на
# одну клетку по горизонтали, или наоборот. Даны две различные клетки шахматной доски,
# определите, может ли конь попасть с первой клетки на вторую одним ходом.

try:
    row1 = int(input('Введите строку 1-ой клетки: '))
    column1 = int(input('Введите столбец 1-ой клетки: '))

    row2 = int(input('Введите строку 2-ой клетки: '))
    column2 = int(input('Введите строку 2-ой клетки: '))

    if row1 + 1 == row2 and column1 + 2 == column2:
        print('YES')
    elif row1 + 1 == row2 and column1 - 2 == column2:
        print('YES')
    elif row1 - 1 == row2 and column1 + 2 == column2:

        print('YES')
    elif row1 + 2 == row2 and column1 - 1 == column2:
        print('YES')
    elif row1 + 2 == row2 and column1 + 1 == column2:
        print('YES')
    elif row1 - 2 == row2 and column1 + 1 == column2:
        print('YES')
    elif row1 - 2 == row2 and column1 - 1 == column2:
        print('YES')
    else:
        print('NO')

except:
    print('Вы ввели некорректное значение')