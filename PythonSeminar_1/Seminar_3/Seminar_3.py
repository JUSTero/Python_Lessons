# -*- coding: cp1251 -*-

# ������ 1. ��� ������ �����. ����������, ������� � ��� ����������� ��������� �����.

# ������ 2.  ���� ������������������ �� N ����� ����� � ����� K. 
# ���������� �������� ��� ������������������ (����� - �����������)
# �� K ��������� ������, K � ������������� �����.

# Task 1
#import random

#some_list = [random.randint(1, 10 ** 9)for i in range(int(input("������� ����� ������: ")))]

#print(f'� ������ {len(set(some_list))} ��������� �����')

# Task 2

import random

some_list = [random.randint(1, 10)for i in range(int(input("������� ����� ������: ")))]
K = int(input('������� ������ ������: '))
temp = K
print(f'��������� ������: {some_list}')

for i in range(K):
	some_list.insert(i,some_list[len(some_list) - K])
	K -= 1

del some_list[-temp:len(some_list)]

print(f'������ �� �������: {some_list}')