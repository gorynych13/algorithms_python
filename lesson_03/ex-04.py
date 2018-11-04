# 4. Определить, какое число в массиве встречается чаще всего.

import random

arr = [random.randint(0, 10) for _ in range(20)]

num_index = 0
count = 0

for i in range(0, len(arr)):
    temp_count = 0
    for j in range(0, len(arr)):
        if arr[i] == arr[j]:
            temp_count += 1
        if temp_count > count:
            count = temp_count
            num_index = i

print(arr)
print(arr[num_index])
