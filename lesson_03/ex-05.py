# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random

arr = [random.randint(-100, 100) for _ in range(20)]

min_negative = arr[0]
for i in arr:
    if i < 0:
        min_negative = i
for i in arr:
    if 0 > i > min_negative:
        min_negative = i

print(arr)
print(min_negative)
