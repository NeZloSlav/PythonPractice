# Дано целое число, не меньшее 2. Выведите его наименьший натуральный делитель, отличный
# от 1.

try:
    num = int(input('Введите число: '))
    div = 2

    if num < 2:
        print('Число должно быть больше 2')
    else:
        while div <= num:
            if num % div == 0:
                print(div)
                break
            else:
                div += 1


except:
    print('Вы ввели некоррекное значение')