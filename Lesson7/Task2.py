# Если объект range (диапазон) передать встроенной в Python функции list(), то она преобразует
# его к списку. Создайте таким образом список с элементами от 0 до 100 и шагом 17.

list_range = range(0, 100, 17)

num_list = list(list_range)

for num in num_list:
    print(num, "", end="")
