# -*- coding: cp1251 -*-

# ������ 2: ������� ����� ���� ������������ �����.

#number = input('������� ���������� �����: ')
#print(f'����� ���� ����� �����: {int(number[0]) + int(number[1]) + int(number[2])}')

# ������ 4: ����, ���� � ������ ������ �� ������ ����������. ������ ��� ������� S ����������. ������� ���������� ������ ������ �������, 
# ���� ��������, ��� ���� � ������ ������� ���������� ���������� ����������, � ���� ������� � ��� ���� ������ ����������, ��� ���� � ������ ������?

S = int(input('������� ���������� ����������: '))
temp = S / 6
P = -(-S // 6)
K = S // 6 * 4
if temp % 1 > 0.5 or S % 2 > 0 or P > K //4:
    print(f'���������� ���������� ������������ �������� ������')
else:
    print(f'����� ������ {P} ����������')
    print(f'���� ������� {K} ����������')
    print(f'���� ������ {P} ����������')
