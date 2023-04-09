# Дано действительное положительное число a и целоe число n.Вычислите an. Решение оформите
# в виде функции power(a, n).Стандартной функцией возведения в степень пользоваться нельзя.

def power(a, n):
    number = a

    for i in range(0, n):
        number *= number
    if n < 0:
        return 1 / number
    else:
        return number


try:
    a = float(input('Введите действительное положительное число a: '))
    if a <= 0:
        print('Число a должно быть положительным!!!')

    n = int(input('Введите целое число n: '))

    print(power(a, n))


except:
    print('Вы ввели некорректное значение')