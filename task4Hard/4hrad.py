# Задача 4 HARD
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


# Комментарий: сначала заполняем список числами Фибоначчи, потом числами негаФибоначчи. По правилам математики - первые два числа чисел Фибоначчи и негаФибоначчи задаются константой

import os
os.system("cls")

negaFib = []
k = int(input('Введите экстремум: ')) # Вводим предел функции негаФибоначчи

for i in range(k+1):                  # Заполняем положительную плоскость в список
    if i == 0 or i == 1:              # Константы положительной плоскости
        negaFib.append(i)
    else:
        negaFib.append(negaFib[i-1] + negaFib[i-2])
print(f"Положительная плоскость: {negaFib}")

negaFib.insert(0,1)                   # Константа отрицательной плоскости
for i in range(k-1) :                   # Заполняем отрицательную плоскость в список
    negaFib.insert(0,negaFib[1]-negaFib[0])

print(f"Последовательность негаФибоначи при {k} порядка: {negaFib}")