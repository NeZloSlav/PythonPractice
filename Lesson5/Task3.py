# Напишите функцию, которая считывает с клавиатуры числа и перемножает их до тех пор, пока
# не будет введен 0. Функция должна возвращать полученное произведение. Вызовите функцию и
# выведите на экран результат ее работы.

def numbers_composition():
    try:
        answer = int(input('Введите число: '))
        composition = answer

        while answer != 0:
            answer = int(input('Введите число: '))
            if answer == 0:
                return composition
            else:
                composition *= answer

    except:
        print('Вы ввели некорректное значение')
        return 0


summary = numbers_composition()
print(summary)
