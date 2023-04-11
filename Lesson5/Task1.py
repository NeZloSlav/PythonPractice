# В основной ветке программы вызывается функция cylinder(), которая
# вычисляет площадь цилиндра. В теле cylinder() определена функция circle(),
# вычисляющая площадь круга по формуле πr 2 . В теле cylinder() у
# пользователя спрашивается, хочет ли он получить только площадь боковой
# поверхности цилиндра, которая вычисляется по формуле 2πrh, или полную
# площадь цилиндра. В последнем случае к площади боковой поверхности
# цилиндра должен добавляться удвоенный результат вычислений функции
# circle().

circle_square = 0
pi = 3.14

def cylinder():

    def circle(radius):
        global circle_square
        circle_square = pi * radius * radius

    print('Что вы хотите получить?\n'
          '1) Площадь боковой поверхности\n'
          '2) Полную площадь')
    answer = input('Введите номер операции: ')

    radius = float(input('Введите радиус: '))
    high = float(input('Введите высоту: '))

    side_square = 2 * pi * radius * high


    if answer == '1':
        print(F'Площадь боковой поверхности {side_square}')
    elif answer == '2':
        circle(radius)
        cylinderSquare = side_square + circle_square * 2
        print(F'Площадь цилиндра {cylinderSquare}')

cylinder()
