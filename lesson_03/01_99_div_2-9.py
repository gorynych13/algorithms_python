# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны любому из чисел в диапазоне от 2 до 9.

# вариант 1
for i in range(2, 10):
    frequency = 0
    for j in range(2, 100):
        if j % i == 0:
            frequency += 1
    print(f'Числу {i} кратно {frequency} чисел')

# вариант 2
frequency = [0] * 8
for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            frequency[j - 2] += 1

for i, item in enumerate(frequency, start=2):
    print(f'Числу {i} кратно {item} чисел')
