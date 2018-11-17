array = [12, 9, 3, 10, 15, 11, 7, 13, 14, 0, 2, 4, 1, 6, 8, 5]

n = 1

while n < len(array):
    for i in range(len(array) - n):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
        print(array)
    n += 1


print(array)
