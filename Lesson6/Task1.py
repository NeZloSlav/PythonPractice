# Напишите программу, которая циклично запрашивает у пользователя номера символов по
# таблице Unicode и выводит соответствующие им символы. Завершает работу при вводе нуля.

try:
    answer = 1

    while answer != 0:
        answer = int(input('Введите номер символа по таблице Unicode: '))
        if answer == 0:
            break
        else:
            print(chr(answer))

except:
    print('Вы ввели некорректное значение')