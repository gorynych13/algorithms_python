# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 10
array = [random.randint(0, SIZE // 1.5) for _ in range(SIZE)]
SIZE = len(array)   # на всякий случай. Вдруг введу готовый массив выше :-)))
print(array)

num = array[0]
frequency = 1
for i in range(SIZE):
    spam = 1
    for k in range(i + 1, SIZE):
        if array[i] == array[k]:
            spam += 1
    if spam > frequency:
        frequency = spam
        num = array[i]

if frequency > 1:
    print(f'Число {num} встречется {frequency} раз(а)')
else:
    print('Все элементы уникальны')

