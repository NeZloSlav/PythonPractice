# Напишите программу, которая запрашивала бы у пользователя два числа и выводила бы True
# или False в зависимости от того, больше первое число второго или нет.

try:
    num_1 = int(input('Enter first number:'))
    num_2 = int(input('Enter second number:'))

    print(num_1 > num_2)

except:
    print('Вы ввели некорректное значение')