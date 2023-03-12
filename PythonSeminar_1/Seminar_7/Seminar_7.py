# -*- coding: cp1251 -*-

# ������ 1. #������� ��������� ������ ����� �� ������������� �������. ������� ����� 
# ������� �������� ��, ������ ������� ����� ����� ������� �������. �������� ������� 
# find_farthest_orbit(list_of_orbits), ������� ����� ������ ����� ������ ������
# ��, �� ������� ��������� ����� ������� �������. �������� ������ �� ����������: 
# �� ������, ��� � ����� ������ ����� ������ ���, ���� ������������� �������� ���� 
# �������� �� �������� ������. ����������� ������� ������ ���� ������, ���������� 
# ����� �������� ������� ������ ����� ������� �������. ������ ������ ������������ 
# �� ���� ������ �� ���� ����� - �������� �� �������. ������� ������� ����������� 
# �� ������� S = pi * a * b, ��� a � b - ����� �������� �������. ��� ������� ������ 
# ����������� ��������� ���������. ���������: ����� ����� ����� ����� ������ � ��� 
# ����: ������� ��������� ����� ������� ������� �������, � ����� ����� � ��� ������, 
# ������� ����� �������. �������������, ��� ����� ������� ������� ����� ����

#def find_farthest_orbit(orbits):
#	maxx = orbits[0]
#	for x in orbits:
#		if x[0] != x[1]:
#			if x[0] * x[1] > maxx[0] * maxx[1]:
#				maxx = x
#	return maxx

#orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
#print(find_farthest_orbit(orbits))

# ������ 2. �������� ������ �� ��������� �����. ������� ����� ��� ���������� ���������� ��������� (��������� �������� � ��� �������, 
# ������� ������ ������ �� ����� �������).

#import random

#def loc_max(sl):
#	for i in range(1, len(sl) - 1):
#		if sl[i - 1] < sl[i] > sl[i + 1]:
#			maxx = i
#	return maxx + 1

#def loc_max_2(sl):
#	for i in range(len(sl) - 2, 0, -1):
#		if sl[i - 1] < sl[i] > sl[i + 1]:
#			return i + 1
#	else:
#		return False

#some_list = [random.randint(1, 10)for i in range(10)]
#print(some_list)
#print(loc_max_2(some_list))

# ������ 3. �������� ������ �� ��������� �����. ������� ������������ ���������� ��� ���������� ���������.

#import random

#def max_repeat(sl):
#	maxx = 1
#	trying = set()
#	for i in sl:
#		if i not in trying:
#			count = sl.count(i)
#			if count > maxx:
#				maxx = count
#				trying.add(i)
#	return maxx

#def max_repeat_2(sl):
#	trying = {}
#	for i in sl:
#		if i not in trying:
#			trying[i] = 1
#		else:
#			trying[i] += 1
#	return trying

#some_list = [random.randint(1, 10)for i in range(10)]
#print(some_list)
#print(max(max_repeat_2(some_list).values()))

# ������ 4. �������� ������ �� ��������� �����. ������� ������ ��������.

#import random

#def second_max(sl):
#	max_1 = sl[0]
#	max_2 = sl[1]
#	if max_1 < max_2:
#		max_1, max_2 = max_2, max_1
#	for i in range(2, len(sl)):
#		if sl[i] > max_1:
#			max_1, max_2 = sl[i], max_1
#		elif sl[i] > max_2:
#			max_2 = sl[i]
#	return max_2

#some_list = [random.randint(1, 10)for i in range(10)]
#print(some_list)
#some_list = list(set(some_list))
#print(second_max(some_list))
#print(some_list)
#some_list.remove(max(some_list))
#print(max(some_list))

