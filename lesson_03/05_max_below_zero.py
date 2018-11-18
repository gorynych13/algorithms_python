# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random

SIZE = 10
array = [random.randint(-1000, -800) for _ in range(SIZE)]
SIZE = len(array)   # на всякий случай. Вдруг введу готовый массив выше :-)))
print(array)

# вариант 1
i = 0
index = -1
while i < SIZE:
    if array[i] < 0 and index == -1:
        index = i
    elif 0 > array[i] > array[index]:
        index = i
    i += 1

if index != -1:
    print(f'Максимальное отрицательное число {array[index]} находится в ячейке {index}')

# вариант 2
num = float('-inf')
index = -1
for i, item in enumerate(array):
    if 0 > item > num:
        num = item
        index = i

if index != -1:
    print(f'Максимальное отрицательное число {num} находится в ячейке {index}')
