# Переменной var_int присвойте значение 10, var_float -значение 8.4, var_str - "No".

var_int = 10
var_float = 8.4
var_str = "No"

# Значение, хранимое в переменной var_int, увеличьте в 3.5 раза.
# Полученный результат свяжите с переменной var_big.

var_big = var_int * 3.5

# Измените значение, хранимое в переменной var_float,
# уменьшив его на единицу, результат свяжите с той же переменной.

var_float = var_float - 1

# Разделите var_int на var_float, а затем var_big на var_float.
# Результат данных выражений не привязывайте ни к каким переменным.

var_int / var_float
var_big / var_float

# Измените значение переменной var_str на "NoNoYesYesYes".
# При формировании нового значения используйте операции конкатенации (+)
# и повторения строки (*).

var_str = var_str + var_str + ("Yes" * 3)

# Выведите значения всех переменных.

print("var_int:", var_int)
print("var_float:", var_float)
print("var_str:", var_str)
print("var_big:", var_big)