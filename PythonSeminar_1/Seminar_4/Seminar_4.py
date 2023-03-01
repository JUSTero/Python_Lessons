# -*- coding: cp1251 -*-

# Задача 1. Напишите программу, которая принимает на вход строку, 
# и отслеживает кол-во повторов каждого символа.

string = input('Введите строку: ')
comp = set()

for i in range(len(string)):
	if string[i] not in comp:
		print(f'"{string[i]}" - {string.count(string[i])}')
		comp.add(string[i])