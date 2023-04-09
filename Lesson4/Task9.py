# Дано действительное положительное число a и целое неотрицательное число n. Вычислите an
# не используя циклы, возведение в степень через ** и функцию math.pow(), а используя
# рекуррентное соотношение an=a⋅an-1.Решение оформите в виде функции power(a, n).

def power(a, n):
    if n == 0:
        return 1

    else:
        return a * power(a, n-1)

try:
    a = float(input('Введите действительное положительное число a: '))
    if a <= 0:
        print('Число a должно быть положительным')

    n = int(input('Введите целое неотрицательное число n: '))
    if n < 0:
        print('Число n должно быть неотрицательным')
    print(power(a, n))


except:
    print('Вы ввели некорректное значение')