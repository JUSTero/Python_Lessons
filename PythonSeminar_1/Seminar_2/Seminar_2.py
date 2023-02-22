# -*- coding: cp1251 -*-

# ������ 1. �� ������� ������ ���������������� n ��������� �������� n!. N! = 1 * 2 * 3 * � * N 
# (������������ ���� ����� �� 1 �� N) 0! = 1 ������ ������ ��������� ���� while

# ������ 2. ���� ����������� ����� A > 1. ����������, ����� �� ����� ������ ��������� ��� ��������, 
# �� ���� �������� ����� ����� n, ��� ?(n)=A. ���� � �� �������� ������ ���������, �������� ����� -1.

# ������ 3. �������� �� �������� ������ ����, ������ ������ ������, ������������� �� ��� ����� ������� �������� �� ��� ������� ���������� �� �������. 
# ��� ���������� � ����������, � ��, � ���� �������, �������� �������������� ���������� �� ������� ����. �� ����������, ������� ���� ������� ����� ������� ��������. 
# ��������� ��� �������� ������, � ������� �������������� ����������� ��������� ��������� 0 �������� �������. �������� ���������, ���������� ���������� � ������.
# ������������ ������ ����� N � ����� ���������� ��������������� ���� (1 ? N ? 100). � ��������� ������� ������������� N ����� �����.
# ������ ����� � �������������� ����������� � ��������������� ����. ����������� � ����� ����� � ����� � ��������� �� �50 �� 50

# Task 1

#n = int(input('������� ����� ��������������� �����: '))
#n1 = n
#N = 1

#while n > 0:
#	N = N * n
#	n -= 1

#print(f'������������ ����� �� 1 �� {n1} ����� {N}')

# Task 2

#A = 0

#while A <= 1:
#	A = int(input('������� ����������� ����� ������ 1: '))

#n = 0
#n1 = 1
#n2 = 0
#count = 2

#while True:
#	n = n2 + n1
#	n2 = n1
#	n1 = n
#	count += 1
#	if n == A:
#		print(f'{A} �������� {count} ������ � ������������������ ���������')
#		break
#	elif n > A:
#		print('-1')
#		break

# Task 3

from random import randint


days = int(input('������� ���������� ��������������� ���� �� 1 �� 100: '))
count = 0
max_days = 0

for i in range(days):
	temp = randint(-51, 51)
	if temp > 0:
		count += 1
		if count > max_days:
			max_days = count
	else:
		count = 0
print(f'����� ������� �������� ���� {max_days} ����')