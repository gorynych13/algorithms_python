# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
array = [random.randint(-100, 100) for _ in range(SIZE)]
print(array)

# 1 вариант
idx_min = 0
idx_max = 0
for i in range(len(array)):
    if array[i] < array[idx_min]:
        idx_min = i
    elif array[i] > array[idx_max]:
        idx_max = i
print(f'Min = {array[idx_min]} в ячейке {idx_min}; Max = {array[idx_max]} в ячейке {idx_max}')

spam = array[idx_min]
array[idx_min] = array[idx_max]
array[idx_max] = spam
print(array)

print('=' * 20)

# 2 вариант как пример асимптотической сложности
# O(n) против O(n) * 4
min_num = min(array)
max_num = max(array)
idx_min = array.index(min_num)
idx_max = array.index(max_num)
print(f'Min = {array[idx_min]} в ячейке {idx_min}; Max = {array[idx_max]} в ячейке {idx_max}')
array[idx_min], array[idx_max] = array[idx_max], array[idx_min]
print(array)
