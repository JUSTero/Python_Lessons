# -*- coding: cp1251 -*-

# Задача 1. Напишите программу, которая принимает на вход строку, 
# и отслеживает кол-во повторов каждого символа.

string = input('Введите строку: ')
comp = []

for i in range(len(string)):
	if string[i] in comp:
		continue
	else:
		print(f'"{string[i]}" - {string.count(string[i])}')
		comp.append(string[i])