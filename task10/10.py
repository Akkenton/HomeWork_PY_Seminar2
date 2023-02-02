# Задача 10:
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

# Комментарий: обозначим значение орла(герба) как 1, а решки как 0. Генерироваться они будут случайным образом. В решении не будем задействовать списки - не опережаем лекционную часть
# Решение будет строится на нахождении количества монеток орлом вверх, и от их количества отталкиваться - если больше чем n/2 то из общего количества вычитаем монтеки орлом вверх, если меньше
# то выводим число монеток орлом вверх

from random import randint
import os
os.system("cls")

orel = 0
n = int(input('Укажите количество монеток: '))

for i in range(n):
    monetka = randint(0,1)
    print(monetka)
    if monetka == 1 : orel += 1
if orel > n // 2 : print(f"Необходимо перевернуть {n - orel} штук")
else : print(f"Необходимо перевернуть {orel} штук")