# -*- coding: cp1251 -*-

# ������ 1. �������� ������� read_last(lines, file), ������� ����� ��������� ������������ ���� file � �������� �� ������ ��������� 
# ��������� ������ � ���������� lines (�� ������ ������ ��������, ��� ������ ������������� ����� �����).

#def out_last_str(lines, file):
#	with open(file, 'r') as file:
#		res = file.read().splitlines()
#		return res[-lines:]

#file = input('������� ��� �����: ')

#lines = 0
#while lines < 1:
#	lines = int(input('������� ���������� �����: '))
#	if lines < 1:
#		print('������� ������������ ��������')

#def print_res(function):
#	for i in function:
#		print(i)

#print_res(out_last_str(lines, file))

# ������ 2. ��������� ����������� ������� longest_words(file), ������� ���������� � ���� result.txt �����, 
# ������� ������������ ����� (��� ������ ����, ���� ������� ���������).

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