# Заполните список случайными числами. Используйте в коде цикл for, функции range() и
# randint().

import random

num_list = []

for i in range(0, 10):
    num = random.randint(1, 100)
    num_list.append(num)

for num in num_list:
    print(num, " ", end="")
