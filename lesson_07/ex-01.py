# array = [12, 9, 3, 10, 15, 11, 7, 13, 14, 0, 2, 4, 1, 6, 8, 5]
# n = 1
# while n < len(array):
#     for i in range(len(array) - 1):
#         if array[i] > array[i + 1]:
#             array[i], array[i + 1] = array[i + 1], array[i]
#     print(array)
#     n += 1
import random

length_arr = int(input("Введите длину массива: "))

array = [random.randint(-100, 99) for _ in range(length_arr)]
print(array)


def bubble_sort(array):
    flag = True
    while flag:
        flag = False
        for i in range(len(array) - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                flag = True
                print(array)

    return array


print(bubble_sort(array))


