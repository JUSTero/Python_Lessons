# -*- coding: cp1251 -*-

# Задача 1. Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить на печать построчно 
# последние строки в количестве lines (на всякий случай проверим, что задано положительное целое число).

#def out_last_str(lines, file):
#	with open(file, 'r') as file:
#		res = file.read().splitlines()
#		return res[-lines:]

#file = input('Введите имя файла: ')

#lines = 0
#while lines < 1:
#	lines = int(input('Введите количество строк: '))
#	if lines < 1:
#		print('Введено недопустимое значение')

#def print_res(function):
#	for i in function:
#		print(i)

#print_res(out_last_str(lines, file))