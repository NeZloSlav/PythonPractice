# Даны три целых числа. Выведите значение наименьшего из них.

try:
    num_1 = int(input('Введите 1-ое число: '))
    num_2 = int(input('Введите 2-ое число: '))
    num_3 = int(input('Введите 3-ье число: '))

    if num_1 < num_2 <= num_3:
        print(num_1)
    elif num_2 < num_1 <= num_3:
        print(num_2)
    else:
        print(num_3)
except:
    print('Вы ввели некорректное значение')