# -*- coding: cp1251 -*-

# 1. ���������� ����� ���� ��������� ����� �����

# 2. ���� ��� ����� �����: A, B. ��������� ���������� ������������: "����� A � B ����� ���������� ��������"

# 3. ������������ ������ ��� ����� �����. �������� ������� �� ���.

# 4. ������������ ������ ����� �����. �������� YES, ���� ��� ����� �������� ��������������, � NO � ��������� ������.

# 5. �� ���� ������ ��������� n ����������. ������� ���� �����, ����� �������� ������� ������ m ����������? 
#   ��� ������� ���� ������ ������ ������������ �������� ����������� if � �������.
# 6. � ��������� ����� ������ ������� ��� ����� �������������� ������ � ����������� �������� ��� ��� 
#   ������ �������. �� ������ ������ ����� ������ ��� ��������. �������� ���������� �������� � ������ �� ���� 
#   �������. �������� ���������� ����� ����, ������� ����� ���������� ��� ���.


# Task 1

#a = int(input("������� ������ �����: "))
#b = int(input("������� ������ �����: "))
#c = int(input("������� ������ �����: "))
#print(f'����� ����� �����: {a + b + c}')

# Task 2

#a = int(input("������� ������ �����: "))
#b = int(input("������� ������ �����: "))

#if a % 2 == b % 2:
#    print('����� ����� ���������� ��������')
#else:
#    print('����� ����� ������ ��������')

# Task 3

#a = int(input("������� ������ �����: "))
#b = int(input("������� ������ �����: "))

#if a < b:
#    print(f'����� {a} ������')
#elif a > b:
#    print(f'����� {b} ������')
#elif a == b:
#    print(f'����� �����')

# Task 4

#a = int(input("������� �����: "))

#if 0 < a //1000 < 10:
#    print('YES')
#else:
#    print('NO')

# Task 5

#N = int(input("������� �������� ��\����: "))
#M = int(input("������� ���� ��: "))

#print (f'������ ������� {M} ���������� �� {(-(-M // N))} ����')

# Task 6

students1 = int(input("������� ����� �������� 1 ������: "))
students2 = int(input("������� ����� �������� 2 ������: "))
students3 = int(input("������� ����� �������� 3 ������: "))
print(f'{(students1 + 1) // 2} ���� ���������� � 1 �����')
print(f'{(students2 + 1) // 2} ���� ���������� � 2 �����')
print(f'{(students3 + 1) // 2} ���� ���������� � 3 �����')
print(f'����� ����� ����: {(1 + students1 + students2 + students3) //2}')