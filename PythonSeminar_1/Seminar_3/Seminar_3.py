# -*- coding: cp1251 -*-

# ������ 1. ��� ������ �����. ����������, ������� � ��� ����������� ��������� �����.

# ������ 2. ���� ������������������ �� N ����� ����� � ����� K. 
# ���������� �������� ��� ������������������ (����� - �����������)
# �� K ��������� ������, K � ������������� �����.

# ������ 3. �������� ��������� ��� ������ ���� ���������� �������� � �������.

# Task 1
#import random

#some_list = [random.randint(1, 10 ** 9)for i in range(int(input("������� ����� ������: ")))]

#print(f'� ������ {len(set(some_list))} ��������� �����')

# Task 2

import random

some_list = [random.randint(1, 10)for i in range(int(input("������� ����� ������: ")))]
K = int(input('������� ������ ������: '))
print(f'��������� ������: {some_list}')

#for i in range(K):
#	some_list.insert(i,some_list[len(some_list) - K])
#	del some_list[len(some_list) - K]
#	K -= 1

#print(f'������ �� �������: {some_list}')

final_list = some_list[K:] + some_list[:K]
print(f'������ �� �������: {final_list}')

# Task 3

