# -*- coding: cp1251 -*-

#with open('example.txt','r') as file:
	#text = file.read()
	#for letter in text:
	#	print(letter)

	#line = file.readline()
	#while line:
	#	print(line)
	#	line = file.readline()

	#text = file.read().splitlines()
	#text2 = text[0].split()
	#print(text2)
	#text = file.readlines()
	#print(text)

#with open('res.txt','a') as file:
#with open('res.txt','w') as file:
#	res = [1, 2, 3, 4]
#	for el in res:
#		file.write(str(el))
#		file.write(str(el) + '\n')

# ������ 1. ������������ ������ �������� ����� � ������, ����� ���������� 
# ����� �������� � ����� � ��������� �������� � ���� res.txt

#count = 0

#with open(input('������� �������� �����: '), 'r') as file:
#	symbol = input('������� ������� ������: ')
#	text = file.read()
#	print(text.count(symbol))
#	line = file.readline()
#	while line:
#		count += line.count(symbol)
#		line = file.readline()


#with open('res.txt', 'w') as file:
#	file.write(str(count))

# ������ 2. ��� ��������� ����, ������� ������ �� ������������� ���� � �������, ������� ������� ������ 3, ���� � ������ 1 �����, �� ������� -1.
# ���������� ������� � ���� res.txt

#res = []

#with open(input('������� �������� �����: '), 'r') as file:
	
#	text = file.read().splitlines()
#	for i in range(0, len(text), 3):
#		temp = text[i].split()
#		if len(temp) < 2:
#			res.append('-1')
#		else:
#			res.append(temp[-2])

#with open('res.txt','w') as file:
#	for el in res:
#		file.write(el + '\n')

#with open(input('������� �������� �����: '), 'r') as file:
#	with open('res.txt','w') as file2:
#		text = file.read().splitlines()
#		for i in range(0, len(text), 3):
#			temp = text[i].split()
#			if len(temp) < 2:
#				file2.write('-1' + '\n')
#			else:
#				file2.write(temp[-2] + '\n')

# ������ 3. ���������� ����� �� ���� ������ � ����.

#with open('res.txt', 'w') as res:
#	with open('test1.txt', 'r') as file:
#		text = file.read().splitlines()
#	with open('test2.txt', 'r') as file:
#		text2 = file.read().splitlines()
#		for el in text:
#			res.write(el + '\n')
#		for el in text2:
#			res.write(el + '\n')

# ������ 4. ��� ��������� ���� � ��������� ����������� �����, � ������ �� ������� �������� ����� �����.
# �������� �����, ����� ����� ����� ����� �� �����, ������� � ����� ���� �������� �����.

#import random

#with open('example.txt', 'w') as file:
#	for i in range(100):
#		file.write(str(random.randint(0,100)) + '\n')

#with open('example.txt', 'r') as file:
#	summa = int(input('������� ������� �����: '))
#	text = file.read().splitlines()
#	flag = 0
#	for i in range(len(text)):
#		if not flag:
#			for j in range(len(text)):
#				if int(text[i]) + int(text[j]) == summa:
#					print(f'{text[i]} + {text[j]} = {summa}')
#					flag = 1
#					break