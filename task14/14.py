# Задача 14:
# Требуется вывести все целые степени двойки (т.е. числа вида 2<sup>k</sup>), не превосходящие числа N.  
# 10 -> 1 2 4 8

import os
os.system('cls')

N = int(input('Введите число: '))

count = 1
i=0
while count <= N :
    print(2**i)
    i += 1
    count = 2**i