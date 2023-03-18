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

# Задача 2. Требуется реализовать функцию longest_words(file), которая записывает в файл result.txt слово, 
# имеющее максимальную длину (или список слов, если таковых несколько).

#def longest_word(file):
#	max_len = 1
#	with open(file, 'r') as file:
#		with open('result.txt', 'a') as res_file:
#			text = file.read()
#			str_list = text.split()
#			for el in str_list:
#				if len(el) > max_len: max_len = len(el)
#			for el in str_list:
#				if len(el) == max_len: res_file.write(el + '\n')

#longest_word('ex.txt')