# Напишите программу, которая запрашивает у пользователя шесть вещественных чисел. На
# экран выводит минимальное и максимальное из них, округленные до двух знаков после запятой.
# Выполните задание без использования встроенных функций min() и max().

array = []

for i in range(0, 6):
    try:
        number = float(input('Введите вещественное число: ').replace(',', '.'))
        array.append(number)
    except:
        print('Вы ввели некорректное значение')
        break

minNumber = maxNumber = array[0]

if len(array) == 6:
    for number in array:
        if number > maxNumber:
            maxNumber = number
        elif number < minNumber:
            minNumber = number

    print(F'Минимальное значение {round(minNumber, 2)}, максимальное значение {round(maxNumber, 2)}')



