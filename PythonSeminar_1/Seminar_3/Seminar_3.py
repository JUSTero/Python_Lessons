# -*- coding: cp1251 -*-

# ������ 1. ��� ������ �����. ����������, ������� � ��� ����������� ��������� �����.

# ������ 2. ���� ������������������ �� N ����� ����� � ����� K.
# ���������� �������� ��� ������������������ (����� - �����������)
# �� K ��������� ������, K � ������������� �����.

# ������ 3. �������� ��������� ��� ������ ���� ���������� �������� � �������.

# ������ 4. ��� ������, ��������� �� ����� �����. �������� ���������,
# ������� ���������� ���������� ��������� �������, ������� �����������
# (�������� � ���������� �������)

# ������ 5. ������ �����:

# �������� ���������� ��������, ����� ������, � ������� ����� ���� �� �����. ����� �������� ���������� ���� � ���� ����� ����� ��� ������.

# ������ ������:

# ��� ������� ����� �������� ����� ������ (���� � 1), � ������� ��� ������ ��� �����������, ��� -1, ���� ������ ����� �� ����.

# 7
# Bessy kept the garden gate,
# And Mary kept the pantry.
# Little Betty Blue Lost her holiday shoe.
# Billy, Billy, come and play.
# Yes, my Polly, so I will.
# Little Bobby Snooks was fond of his books.
# Robert Barnes, my fellow fine, can you shoe this horse of mine?

# ������ �����:

# 4
# Mary
# Jack
# Billy
# Bobby

# ������ ������:

# 2
# -1
# 4
# 6

# ������ 6. ���� ������ �����, ������ ����� ����� n. ������, ���� �� � ������ ����� 2 �����, 
# ��� �� ����� ����� ����� n.

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

# import random

# some_list = [random.randint(1, 10)for i in range(int(input("������� ����� ������: ")))]
# print(f'��������� ������: {some_list}')
# count = 0

# for i in range(1,len(some_list)):
# 	if some_list[i] > some_list[i - 1]:
# 		count += 1
# print(f'���������� ��������� �������, ������� �����������: {count}')

# Task 5

# text_list = ['Bessy kept the garden gate,' , 'And Mary kept the pantry.' , 'Little Betty Blue Lost her holiday shoe.' , 'Billy, Billy, come and play.' , 'Yes, my Polly, so I will.' ,
# 'Little Bobby Snooks was fond of his books.' , 'Robert Barnes, my fellow fine, can you shoe this horse of mine?']
##text_list = [input() for i in range(int(input("������ ���������� �����: ")))]
# print(text_list)
# name_list = ['Mary' , 'Jack' , 'Billy' , 'Bobby']
##name_list = [input() for i in range(int(input("������� ���������� ���: ")))]
# print(name_list)

# for i in range(len(name_list)):
# 	mark = -1
# 	for j in range(len(text_list)):
# 		if name_list[i] in text_list[j]:
# 			mark = j + 1
# 	print(mark)

# Task 6

#import random

#some_list = [random.randint(1, 100)for i in range(int(input("������� ����� ������: ")))]
#print(f'��������� ������: {some_list}')
#n = int(input('������� ������� ����� n: '))
#some_set = set(some_list)

#for i in some_set:
#	if n - i in some_set:
#		print(f'{i} + {n - i} YES')
#		break
#else:
#	print('NO')

## import time
## start = time.perf_counter()
