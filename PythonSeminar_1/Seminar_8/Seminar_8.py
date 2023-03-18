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
	#text = file.readlines()
	#print(text)

#with open('res.txt','a') as file:
#with open('res.txt','w') as file:
#	res = [1, 2, 3, 4]
#	for el in res:
#		file.write(str(el))
#		file.write(str(el) + '\n')

# Задача 1. Пользователь вводит название файла и символ, найти количество 
# таких символов в файле и результат записать в файл res.txt

#count = 0

#with open(input('Введите название файла: '), 'r') as file:
#	symbol = input('Введите искомый символ: ')
#	line = file.readline()
#	while line:
#		count += line.count(symbol)
#		line = file.readline()


#with open('res.txt', 'w') as file:
#	file.write(str(count))