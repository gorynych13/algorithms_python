# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив
# надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 – если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

import random

arr = [random.randint(0, 100) for _ in range(20)]
even_arr = []
odd_arr = []

for i in range(0, len(arr)):
    if arr[i] % 2 == 0:
        even_arr.append(i)
    else:
        odd_arr.append(i)

print(arr)
print(even_arr)
print(odd_arr)
