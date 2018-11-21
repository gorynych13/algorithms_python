import random


def mediana_array(array):

    for i in range(len(array)):
        no_more = 0
        no_less = 0
        is_equal = 0
        for j in range(len(array)):
            if i == j:
                continue
            if array[i] < array[j]:
                no_less += 1
            elif array[i] > array[j]:
                no_more += 1
            else:
                is_equal += 1

        if no_more == no_less:
            return array[i]
        # Вот тут выглядит как костыль, но ничего лучше пока придумать не смог
        if no_more <= len(array) // 2 and no_less <= len(array) // 2 and is_equal >= 1:
            return array[i]


m = int(input("Input array length:"))
n = 2 * m + 1

array = [random.randint(1, 100) for _ in range(n)]
print(array)
print(f"Медиана массива = {mediana_array(array)}")
array.sort()
print(array)




