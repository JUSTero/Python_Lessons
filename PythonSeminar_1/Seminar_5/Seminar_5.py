# -*- coding: cp1251 -*-

# ������ 1.  ������������������� ��������� ���������� ������������������ ����� a0, a1, ..., an,
#  ..., ��� a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1). ��������� ����� N-� ����� ���������

#N = int(input(f'������� �����: '))

#def fib(n):
#	a = 0
#	b = 1
#	f = 0

#	if n == 1: 
#		print(b)
#	elif n ==0: 
#		print(a)
#	else:
#		for i in range(2, n + 1):
#			f = a + b
#			a = b
#			b = f
#	return f

#print(fib(N))

#N = int(input(f'������� �����: '))

#def fib(n):
#	if n == 0: 
#		return 0
#	elif n == 1: 
#		return 1
#	return fib(n - 1) + fib(n - 2)

#print(fib(N))

# ������ 2. ����� ������� ������� ������ � ��������� ������� � ����� �������� ��� ���� ���������� ������ �� ������������. 
# �������� ���������. ������� ������� ������ �������. �� ��������: ��� ������������ - �� �����������.

#estimates = [5, 4, 5, 3, 3, 2, 5, 3, 4, 3, 5, 4, 3, 2, 2, 3, 4, 5, 5, 5, 4, 5, 4]
#print(estimates)

#def fix_estimates(est):
#	maximum = max(est)
#	minimum = min(est)

#	for i in range(len(est)):
#		if est[i] == maximum:
#			est[i] = minimum
#	return(est)

#print(fix_estimates(estimates))

# ������ 3.  �������� �������, ������� ��������� ���� ����� � ���������, �������� �� ��� �������
# *�����������: ������� ����� - ��� �����, ������� ����� 2 ��������: 1  � n(���� �����)*

#n = int(input('������� �����: '))
#count = True

#if n < 4:
#	print(count)
#else:
#	for i in range(2, n // 2 + 1):
#		if n % i == 0:
#			count = False
#			break

#print(count)