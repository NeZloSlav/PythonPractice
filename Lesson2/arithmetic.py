# Напишите программу (файл arithmetic.py), которая предлагала бы пользователю решить пример
# 4 * 100 - 54. Потом выводила бы на экран правильный ответ и ответ пользователя. Подумайте,
# нужно ли здесь преобразовывать строку в число.

action = input('Не хотите ли решить пример?\n1)Давай\n2)Не сейчас\n')
if action == "1":
    print("Пример: 4 * 100 - 54")
    answer = input('Введите ответ: ')

    print("Ваш ответ: " + answer)
    print("Правильный ответ: 346")

else:
    print("Хорошо, увидимся позже)")