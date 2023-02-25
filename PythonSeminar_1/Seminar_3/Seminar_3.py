# -*- coding: cp1251 -*-

# Задача 1. Дан список чисел. Определите, сколько в нем встречается различных чисел.

# Task 1
import random

some_list = [random.randint(1, 10 ** 9)for i in range(int(input("Введите длину списка: ")))]
print(f'В списке {len(set(some_list))} различных чисел')