import random


def merge_sort(array):

    N = len(array)

    # Exit recursion
    if N == 1:
        return array

    # Make sub_arrays
    left_array = array[0: N//2]
    right_array = array[N//2: N + 1]

    left_array = merge_sort(left_array)
    right_array = merge_sort(right_array)

    # make merge
    exit_array = [None] * N

    left_current = 0
    right_current = 0

    for i in range(N):
        if left_current < len(left_array) and right_current < len(right_array):
            if left_array[left_current] < right_array[right_current]:
                exit_array[i] = left_array[left_current]
                left_current += 1
            else:
                exit_array[i] = right_array[right_current]
                right_current += 1
        elif left_current < len(left_array):
            exit_array[i] = left_array[left_current]
            left_current += 1
        else:
            exit_array[i] = right_array[right_current]
            right_current += 1

    return exit_array


array = [int(random.uniform(0, 49.9999999)*1000) / 1000 for _ in range(20)]
print(array)
print(merge_sort(array))






