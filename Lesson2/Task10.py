# В математике функция sign(x) (знак числа) определена так:
# sign(x) = 1, если x &amp;gt; 0,
# sign(x) = -1, если x &amp;lt; 0,
# sign(x) = 0, если x = 0.
# Для данного числа x выведите значение sign(x). Эту задачу желательно решить с использованием
# каскадных инструкций if... elif... else.

try:
    x = int(input('Введите значение x: '))

    if x < 0:
        print('sign(x) = -1')
    elif x > 0:
        print('sign(x) = 1')
    else:
        print('sign(x) = 0')

except:
    print('Вы ввели некорректное значение')