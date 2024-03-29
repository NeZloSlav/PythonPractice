# Вклад в банке составляет x рублей. Ежегодно он увеличивается на p процентов, после чего
# дробная часть копеек отбрасывается. Определите, через сколько лет вклад составит не менее y
# рублей. Выражение «дробная часть копеек отбрасывается» означает, что если у вас оказалось
# 123.4567 рублей, т. е. 123 рубля и 45.67 копеек, то после округления у вас получится 123 рубля и
# 45 копеек, т.е. 123.45 рублей. Программа получает на вход три натуральных числа: x, p, y и должна
# вывести одно целое число.

try:
    x = int(input('Вклад в банке состовляет: '))
    p = int(input('Ежегодно он увеличивается на (процент): '))
    y = int(input('Через сколько лет вклад составит не менее: '))

    years = 0

    while x < y:
        x *= 1 + p / 100
        x = int(100 * x) / 100
        years += 1

    print(years)

except:
    print('Вы ввели некорректное значение')