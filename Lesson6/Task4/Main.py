from MyModule import rectangle, triangle, circle

answer = input('Площадь чего вы хотите найти?\n1)Прямоугольника\n2)Треугольника\n3)Окружности\n')

match answer:
    case '1':
        try:
            print(rectangle(int(input('Введите длину: ')), int(input('Введите ширину: '))))
        except:
            print('Вы ввели некорректное значение')
    case '2':
        try:
            print(triangle(int(input('Введите длину стороны: ')), int(input('Введите высоту: '))))
        except:
            print('Вы ввели некорректное значение')
    case '3':
        try:
            print(circle(int(input('Введите радиус: '))))
        except:
            print('Вы ввели некорректное значение')
    case _:
        print("Такого варианта ответа нет")
