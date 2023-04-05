# Шахматный ферзь ходит по диагонали, горизонтали или вертикали. Даны две различные клетки
# шахматной доски, определите, может ли ферзь попасть с первой клетки на вторую одним ходом.

try:
    row1 = int(input('Введите строку 1-ой клетки: '))
    column1 = int(input('Введите столбец 1-ой клетки: '))

    row2 = int(input('Введите строку 2-ой клетки: '))
    column2 = int(input('Введите строку 2-ой клетки: '))

    if row1 == row2 or column1 == column2:
        print('YES')
    elif abs(row1 - row2) == abs(column1 - column2):
        print('YES')
    else:
        print('NO')

except:
    print('Вы ввели некорректное значение')