﻿# Задача 2: Найдите сумму цифр трехзначного числа.

# number = input('Введите трёхзначное число: ')
# print(f'Сумма цифр числа равна: {int(number[0]) + int(number[1]) + int(number[2])}')

###

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# S = int(input('Введите количество журавликов: '))
# temp = S / 6
# P = -(-S // 6)
# K = S // 6 * 4
# if temp % 1 > 0.5 or S % 2 > 0 or P > K //4:
#    print(f'Количество журавликов противоречит условиям задачи')
# else:
#    print(f'Серёжа сделал {P} журавликов')
#    print(f'Катя сделала {K} журавликов')
#    print(f'Петя сделал {P} журавликов')

###

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

#number = input('Введите номер билета: ')
#if int(number[0]) + int(number[1]) + int(number[2]) == int(number[3]) + int(number[4]) + int(number[5]):
#    print('Счачтливый билет!!!')
#else:
#    print('Обычный билет')

###

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

#n = int(input('Введите длину: '))
#m = int(input('Введите ширину: '))
#k = int(input('Введите количество долек: '))

#if (k < m * n) and (k % n == 0 or k % m == 0):
#    print('YES')
#else:
#    print('NO')