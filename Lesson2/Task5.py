# Дано число n. С начала суток прошло n минут. Определите, сколько часов и минут будут
# показывать электронные часы в этот момент. Программа должна вывести два числа: количество
# часов (от 0 до 23) и количество минут (от 0 до 59). Учтите, что число n может быть больше, чем
# количество минут в сутках.

try:
    quantity_of_minutes = int(input('С начала суток прошло:'))
    quantity_of_hours = quantity_of_minutes // 60
    remaining_minutes = quantity_of_minutes % 60

    if quantity_of_hours > 23:
        days = quantity_of_hours // 24
        quantity_of_hours = quantity_of_hours - days * 24
        if remaining_minutes < 10:
            print(F'Прошло {days} д. Время: {quantity_of_hours}:0{remaining_minutes}')
        else:
            print(F'Прошло {days} д. Время: {quantity_of_hours}:{remaining_minutes}')

    else:
        if remaining_minutes < 10:
            print(F'Время: {quantity_of_hours}:0{remaining_minutes}')

except:
    print('Вы ввели некорректное значение')