# Задача 5 HARD
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в N-мерном пространстве.
# Сначала задается N с клавиатуры, потом задаются координаты точек.

# Расстояния в многомерном пространстве рассчитывается через формулу расстояния Евклида

from math import sqrt
import os
os.system('cls')


N = int(input('Введите количество пространств: '))
summ = 0
A = "A("
B = "B("
for i in range(N) :
    coord1 = input(f"Введите координату точки А в {i} пространстве: ")
    coord2 = input(f"Введите координату точки B в {i} пространстве: ")
    A += coord1 + ','
    B += coord2 + ','
    summ += (int(coord1)-int(coord2))**2
    print(summ)
A = A[:-1]
B = B[:-1]
A += ')'
B += ')'
print(A)
print(B)
print(f"Расстояние между точкам в {N} мерном пространстве равно: {round(sqrt(summ),3)}")