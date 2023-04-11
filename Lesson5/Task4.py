# 1. Функция getInput() не имеет параметров, запрашивает ввод с клавиатуры и возвращает в
# основную программу полученную строку.
# 2. Функция testInput() имеет один параметр. В теле она проверяет, можно ли переданное ей
# значение преобразовать к целому числу. Если можно, возвращает логическое True. Если нельзя –
# False.
# 3. Функция strToInt() имеет один параметр. В теле преобразовывает переданное значение к
# целочисленному типу. Возвращает полученное число.
# 4. Функция printInt() имеет один параметр. Она выводит переданное значение на экран и ничего
# не возвращает.

def getInput():
    input_string = input('Введите строку: ')
    return input_string


def testInput(line):
    try:
        number = int(line)
        return True
    except:
        return False


def strToInt(line):
    string_to_int = int(line)
    return string_to_int


def printInt(integer):
    print(integer)


something = getInput()
if testInput(something):
    printInt(strToInt(something))



