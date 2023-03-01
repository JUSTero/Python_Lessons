# -*- coding: cp1251 -*-

# Задача 1. Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах. Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств. (Попробуйте использовать множества и их пересечение)

# import random

# some_list1 = [random.randint(1, 100)for i in range(int(input("Введите длину списка1: ")))]
# some_list2 = [random.randint(1, 100)for i in range(int(input("Введите длину списка2: ")))]
# some_set1 = set(some_list1)
# some_set2 = set(some_list2)
# final_set = set()
# print(some_set1)
# print(some_set2)

# if len(some_set1) >= len(some_set2):
# 	for i in some_set1:
# 		if i in some_set2:
# 			final_set.add(i)
# else:
# 	for i in some_set2:
# 		if i in some_set1:
# 			final_set.add(i)

# print(final_set)

# some_list1 = [random.randint(1, 100)for i in range(int(input("Введите длину списка1: ")))]
# some_list2 = [random.randint(1, 100)for i in range(int(input("Введите длину списка2: ")))]
# some_set1 = set(some_list1)
# some_set2 = set(some_list2)
# print(sorted(some_set1.intersection(some_set2)))

