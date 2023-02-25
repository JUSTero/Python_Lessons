# -*- coding: cp1251 -*-

# Задача 1. Дан список чисел. Определите, сколько в нем встречается различных чисел.

# Задача 2. Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический)
# на K элементов вправо, K – положительное число.

# Задача 3. Напишите программу для печати всех уникальных значений в словаре.

# Task 1
#import random

#some_list = [random.randint(1, 10 ** 9)for i in range(int(input("Введите длину списка: ")))]

#print(f'В списке {len(set(some_list))} различных чисел')

# Task 2

import random

some_list = [random.randint(1, 10)for i in range(int(input("Введите длину списка: ")))]
K = int(input('Введите размер сдвига: '))
print(f'Начальный список: {some_list}')

#for i in range(K):
#	some_list.insert(i,some_list[len(some_list) - K])
#	del some_list[len(some_list) - K]
#	K -= 1

#print(f'Список со сдвигом: {some_list}')

final_list = some_list[K:] + some_list[:K]
print(f'Список со сдвигом: {final_list}')

# Task 3

