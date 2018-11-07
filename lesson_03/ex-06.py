# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и
# максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

import random

arr = [random.randint(0, 100) for _ in range(10)]

print(arr)
print()

max_index = 0
min_index = 0
sum_numbers = 0

for i in range(0, len(arr)):
    if arr[max_index] < arr[i]:
        max_index = i
    if arr[min_index] > arr[i]:
        min_index = i

print("Сумма", end=" ")

for i in range(0, len(arr)):
    if arr[i] != arr[max_index] and arr[i] != arr[min_index]:
        print(arr[i], end=" ")
        sum_numbers += arr[i]

print(f"= {sum_numbers}")

print()
print(f"Минимальное число - {arr[min_index]}")
print(f"Максимальное число - {arr[max_index]}")

