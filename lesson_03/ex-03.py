# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

arr = [random.randint(0, 100) for _ in range(20)]

print(arr)

max_index = 0
min_index = 0

for i in range(0, len(arr)):
    if arr[max_index] < arr[i]:
        max_index = i
    if arr[min_index] > arr[i]:
        min_index = i

arr[max_index], arr[min_index] = arr[min_index], arr[max_index]

print(arr)
