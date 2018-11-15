# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random
import sys


def show_size(x, level=0):
    all_size = 0
    print('\t' * level, f'type = {type(x)}, size = {sys.getsizeof(x)}, object = {x}')
    all_size += sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show_size(key, level + 1)
                all_size += sys.getsizeof(key)
                show_size(value, level + 1)
                all_size += sys.getsizeof(value)

        elif not isinstance(x, str):
            for item in x:
                show_size(item, level + 1)
                all_size += sys.getsizeof(item)

    return all_size



arr = [random.randint(0, 100) for _ in range(10)]

print(arr)

max_index = 0
min_index = 0

for i in range(0, len(arr)):
    if arr[max_index] < arr[i]:
        max_index = i
    if arr[min_index] > arr[i]:
        min_index = i

spam = arr[max_index]
arr[max_index] = arr[min_index]
arr[min_index] = spam
#arr[max_index], arr[min_index] = arr[min_index], arr[max_index]


print(arr)
print()


file_size = [show_size(arr), show_size(max_index), show_size(min_index), show_size(spam),
             show_size(len(arr))]

print(f"Общий размер {sum(file_size)} байт")


# Не понял как с циклом быть и переменной i
# Плюс как говорилось в уроке числа от 0 до 255 заранее зарезервированы в памяти,
# получается лишнего переменная i не занимает в памяти
# [41, 90, 90, 17, 95, 2, 81, 1, 61, 97]
# [41, 90, 90, 17, 95, 2, 81, 97, 61, 1]
#
#  type = <class 'list'>, size = 192, object = [41, 90, 90, 17, 95, 2, 81, 97, 61, 1]
# 	 type = <class 'int'>, size = 28, object = 41
# 	 type = <class 'int'>, size = 28, object = 90
# 	 type = <class 'int'>, size = 28, object = 90
# 	 type = <class 'int'>, size = 28, object = 17
# 	 type = <class 'int'>, size = 28, object = 95
# 	 type = <class 'int'>, size = 28, object = 2
# 	 type = <class 'int'>, size = 28, object = 81
# 	 type = <class 'int'>, size = 28, object = 97
# 	 type = <class 'int'>, size = 28, object = 61
# 	 type = <class 'int'>, size = 28, object = 1
#  type = <class 'int'>, size = 28, object = 9
#  type = <class 'int'>, size = 28, object = 7
#  type = <class 'int'>, size = 28, object = 97
#  type = <class 'int'>, size = 28, object = 10
# Общий размер 584 байт
print("*" * 70)

# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив
# надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 – если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.


arr1 = [random.randint(0, 100) for _ in range(20)]
even_arr = []
odd_arr = []

for i in range(0, len(arr1)):
    if arr1[i] % 2 == 0:
        even_arr.append(i)
    else:
        odd_arr.append(i)

print(f"Исходный массив {arr1}")
print(f"Четные индексы {even_arr}")
print(f"Нечетные индексы {odd_arr}")

all_arrays_size = [show_size(arr1), show_size(even_arr), show_size(odd_arr)]

print(f"Общий размер {sum(all_arrays_size)} байт")


# Исходный массив [80, 49, 53, 42, 76, 55, 20, 6, 49, 90, 65, 53, 48, 51, 0, 23, 16, 6, 54, 85]
# Четные индексы [0, 3, 4, 6, 7, 9, 12, 14, 16, 17, 18]
# Нечетные индексы [1, 2, 5, 8, 10, 11, 13, 15, 19]
#  type = <class 'list'>, size = 264, object =
# [80, 49, 53, 42, 76, 55, 20, 6, 49, 90, 65, 53, 48, 51, 0, 23, 16, 6, 54, 85]
# 	 type = <class 'int'>, size = 28, object = 80
# 	 type = <class 'int'>, size = 28, object = 49
# 	 type = <class 'int'>, size = 28, object = 53
# 	 type = <class 'int'>, size = 28, object = 42
# 	 type = <class 'int'>, size = 28, object = 76
# 	 type = <class 'int'>, size = 28, object = 55
# 	 type = <class 'int'>, size = 28, object = 20
# 	 type = <class 'int'>, size = 28, object = 6
# 	 type = <class 'int'>, size = 28, object = 49
# 	 type = <class 'int'>, size = 28, object = 90
# 	 type = <class 'int'>, size = 28, object = 65
# 	 type = <class 'int'>, size = 28, object = 53
# 	 type = <class 'int'>, size = 28, object = 48
# 	 type = <class 'int'>, size = 28, object = 51
# 	 type = <class 'int'>, size = 24, object = 0
# 	 type = <class 'int'>, size = 28, object = 23
# 	 type = <class 'int'>, size = 28, object = 16
# 	 type = <class 'int'>, size = 28, object = 6
# 	 type = <class 'int'>, size = 28, object = 54
# 	 type = <class 'int'>, size = 28, object = 85
#  type = <class 'list'>, size = 192, object = [0, 3, 4, 6, 7, 9, 12, 14, 16, 17, 18]
# 	 type = <class 'int'>, size = 24, object = 0
# 	 type = <class 'int'>, size = 28, object = 3
# 	 type = <class 'int'>, size = 28, object = 4
# 	 type = <class 'int'>, size = 28, object = 6
# 	 type = <class 'int'>, size = 28, object = 7
# 	 type = <class 'int'>, size = 28, object = 9
# 	 type = <class 'int'>, size = 28, object = 12
# 	 type = <class 'int'>, size = 28, object = 14
# 	 type = <class 'int'>, size = 28, object = 16
# 	 type = <class 'int'>, size = 28, object = 17
# 	 type = <class 'int'>, size = 28, object = 18
#  type = <class 'list'>, size = 192, object = [1, 2, 5, 8, 10, 11, 13, 15, 19]
# 	 type = <class 'int'>, size = 28, object = 1
# 	 type = <class 'int'>, size = 28, object = 2
# 	 type = <class 'int'>, size = 28, object = 5
# 	 type = <class 'int'>, size = 28, object = 8
# 	 type = <class 'int'>, size = 28, object = 10
# 	 type = <class 'int'>, size = 28, object = 11
# 	 type = <class 'int'>, size = 28, object = 13
# 	 type = <class 'int'>, size = 28, object = 15
# 	 type = <class 'int'>, size = 28, object = 19
# Общий размер 1760 байт
