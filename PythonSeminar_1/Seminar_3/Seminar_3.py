# -*- coding: cp1251 -*-

# Задача 1. Дан список чисел. Определите, сколько в нем встречается различных чисел.

# Задача 2. Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический)
# на K элементов вправо, K – положительное число.

# Задача 3. Напишите программу для печати всех уникальных значений в словаре.

# Задача 4. Дан массив, состоящий из целых чисел. Напишите программу,
# которая подсчитает количество элементов массива, больших предыдущего
# (элемента с предыдущим номером)

# Task 1

# import random

# some_list = [random.randint(1, 10 ** 9)for i in range(int(input("Введите длину списка: ")))]

# print(f'В списке {len(set(some_list))} различных чисел')

# Task 2

# import random

# some_list = [random.randint(1, 10)for i in range(int(input("Введите длину списка: ")))]
# K = int(input('Введите размер сдвига: '))
# print(f'Начальный список: {some_list}')

# for i in range(K):
# 	some_list.insert(i,some_list[len(some_list) - K])
# 	del some_list[len(some_list) - K]
# 	K -= 1

# print(f'Список со сдвигом: {some_list}')

# final_list = some_list[K:] + some_list[:K]
# print(f'Список со сдвигом: {final_list}')

# Task 3

# some_dict = {1 : 3, 2 : 4, 3 : 4}

# print(f'Уникальные значения словаря: {set(some_dict.values())}')

# Task 4

import random

some_list = [random.randint(1, 10)for i in range(int(input("Введите длину списка: ")))]
print(f'Начальный список: {some_list}')
count = 0

for i in range(1,len(some_list)):
	if some_list[i] > some_list[i - 1]:
		count += 1
print(f'Количество элементов массива, больших предыдущего: {count}')
