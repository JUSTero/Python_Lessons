# -*- coding: cp1251 -*-

# ������ 1. ��� ������ �����. ����������, ������� � ��� ����������� ��������� �����.

# Task 1
import random

some_list = [random.randint(1, 10 ** 9)for i in range(int(input("������� ����� ������: ")))]
print(f'� ������ {len(set(some_list))} ��������� �����')