# -*- coding: cp1251 -*-

# ������ 1. �������� ���������, ������� ��������� �� ���� ������, 
# � ����������� ���-�� �������� ������� �������.

string = input('������� ������: ')
comp = []

for i in range(len(string)):
	if string[i] in comp:
		continue
	else:
		print(f'"{string[i]}" - {string.count(string[i])}')
		comp.append(string[i])