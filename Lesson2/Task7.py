# Присвойте двум переменным любые числовые значения.

num_1 = 5
num_2 = 4

# Используя переменные из п. 1, с помощью оператора "and" составьте два сложных логических
# выражения, одно из которых дает истину, другое – ложь.

if num_1 + num_2 == 9 and num_1 + num_2 < 10:
    print('Condition 1')

if num_1 * num_2 <= 100 and num_1 % num_2 == 0:
    print('Condition 2')

# Аналогично выполните п. 2, но уже с оператором "or".

if num_2 - num_1 < 3 or num_2 / num_1 > 2:
    print('Condition 3')

if num_1 + num_2 <= 3 or num_1 * num_2 >= 100:
    print('Condition 4')

# Попробуйте использовать в логических выражениях переменные строкового типа. Объясните
# результат.

str_1 = "Yes"
str_2 = "No"

if str_1 == str_2:
    print('Condition 5')

str_3 = ""
str_4 = " "

if str_3 + str_4 == str_4:
    print('Condition 6')