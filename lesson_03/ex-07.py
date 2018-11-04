# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

arr = [random.randint(0, 100) for _ in range(20)]

min_index_1 = 0
for i in range(0, len(arr)):
    if arr[min_index_1] > arr[i]:
        min_index_1 = i

min_index_2 = 0
if min_index_1 == len(arr) - 1:
    min_index_2 = min_index_1 - 1
else:
    min_index_2 = min_index_1 + 1


for i in range(0, len(arr)):
    if i == min_index_1:
        continue
    if arr[min_index_2] > arr[i]:
        min_index_2 = i

print(arr)
print(arr[min_index_1])
print(arr[min_index_2])
