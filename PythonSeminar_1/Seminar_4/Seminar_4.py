# -*- coding: cp1251 -*-

# ������ 1. �������� ���������, ������� ��������� �� ���� ������, 
# � ����������� ���-�� �������� ������� �������.

string = input('������� ������: ')
comp = set()

for i in range(len(string)):
	if string[i] not in comp:
		print(f'"{string[i]}" - {string.count(string[i])}')
		comp.add(string[i])