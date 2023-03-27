# Напишите программу (файл user.py), которая запрашивала бы у пользователя:
# - его имя (например, "What is your name?")
# - возраст ("How old are you?")
# - место жительства ("Where are you live?")
# После этого выводила бы три строки:
# This is (имя)
# It is (возраст)
# (S)he live in (место_жительства)

try:
    print('Welcome, Dear friend!')
    name = input('What is your name? - ')
    age = int(input('How old are you? - '))
    location = input('Where are you live? - ')

    print('This is', name)
    print(F'It is {age}')
    print('(S)he live in ' + location)

except:
    print('Вы ввели некорректное значение')