# -*- coding: cp1251 -*-

# Задача 1. Дан список чисел. Определите, сколько в нем встречается различных чисел.

# Задача 2. Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический)
# на K элементов вправо, K – положительное число.

# Задача 3. Напишите программу для печати всех уникальных значений в словаре.

# Задача 4. Дан массив, состоящий из целых чисел. Напишите программу,
# которая подсчитает количество элементов массива, больших предыдущего
# (элемента с предыдущим номером)

# Задача 5. Формат ввода:

# Вводится количество играющих, затем строки, в которых могут быть их имена. Затем вводится количество имен и сами имена детей для поиска.

# Формат вывода:

# Для каждого имени выведите номер строки (счет с 1), в которой оно первый раз встретилось, или -1, если такого имени не было.

# 7
# Bessy kept the garden gate,
# And Mary kept the pantry.
# Little Betty Blue Lost her holiday shoe.
# Billy, Billy, come and play.
# Yes, my Polly, so I will.
# Little Bobby Snooks was fond of his books.
# Robert Barnes, my fellow fine, can you shoe this horse of mine?

# Пример ввода:

# 4
# Mary
# Jack
# Billy
# Bobby

# Пример вывода:

# 2
# -1
# 4
# 6

# Задача 6. Есть список чисел, вводят некое число n. Понять, есть ли в списке такие 2 числа, 
# что их сумма будет равна n.

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

# import random

# some_list = [random.randint(1, 10)for i in range(int(input("Введите длину списка: ")))]
# print(f'Начальный список: {some_list}')
# count = 0

# for i in range(1,len(some_list)):
# 	if some_list[i] > some_list[i - 1]:
# 		count += 1
# print(f'Количество элементов массива, больших предыдущего: {count}')

# Task 5

# text_list = ['Bessy kept the garden gate,' , 'And Mary kept the pantry.' , 'Little Betty Blue Lost her holiday shoe.' , 'Billy, Billy, come and play.' , 'Yes, my Polly, so I will.' ,
# 'Little Bobby Snooks was fond of his books.' , 'Robert Barnes, my fellow fine, can you shoe this horse of mine?']
##text_list = [input() for i in range(int(input("Ввдите количество строк: ")))]
# print(text_list)
# name_list = ['Mary' , 'Jack' , 'Billy' , 'Bobby']
##name_list = [input() for i in range(int(input("Введите количество имён: ")))]
# print(name_list)

# for i in range(len(name_list)):
# 	mark = -1
# 	for j in range(len(text_list)):
# 		if name_list[i] in text_list[j]:
# 			mark = j + 1
# 	print(mark)

# Task 6

#import random

#some_list = [random.randint(1, 100)for i in range(int(input("Введите длину списка: ")))]
#print(f'Начальный список: {some_list}')
#n = int(input('Введите искомое число n: '))
#some_set = set(some_list)

#for i in some_set:
#	if n - i in some_set:
#		print(f'{i} + {n - i} YES')
#		break
#else:
#	print('NO')

## import time
## start = time.perf_counter()
