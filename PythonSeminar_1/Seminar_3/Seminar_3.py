# -*- coding: cp1251 -*-

# ������ 1. ��� ������ �����. ����������, ������� � ��� ����������� ��������� �����.

# ������ 2. ���� ������������������ �� N ����� ����� � ����� K.
# ���������� �������� ��� ������������������ (����� - �����������)
# �� K ��������� ������, K � ������������� �����.

# ������ 3. �������� ��������� ��� ������ ���� ���������� �������� � �������.

# ������ 4. ��� ������, ��������� �� ����� �����. �������� ���������,
# ������� ���������� ���������� ��������� �������, ������� �����������
# (�������� � ���������� �������)

# Task 1

# import random

# some_list = [random.randint(1, 10 ** 9)for i in range(int(input("������� ����� ������: ")))]

# print(f'� ������ {len(set(some_list))} ��������� �����')

# Task 2

# import random

# some_list = [random.randint(1, 10)for i in range(int(input("������� ����� ������: ")))]
# K = int(input('������� ������ ������: '))
# print(f'��������� ������: {some_list}')

# for i in range(K):
# 	some_list.insert(i,some_list[len(some_list) - K])
# 	del some_list[len(some_list) - K]
# 	K -= 1

# print(f'������ �� �������: {some_list}')

# final_list = some_list[K:] + some_list[:K]
# print(f'������ �� �������: {final_list}')

# Task 3

# some_dict = {1 : 3, 2 : 4, 3 : 4}

# print(f'���������� �������� �������: {set(some_dict.values())}')

# Task 4

import random

some_list = [random.randint(1, 10)for i in range(int(input("������� ����� ������: ")))]
print(f'��������� ������: {some_list}')
count = 0

for i in range(1,len(some_list)):
	if some_list[i] > some_list[i - 1]:
		count += 1
print(f'���������� ��������� �������, ������� �����������: {count}')
