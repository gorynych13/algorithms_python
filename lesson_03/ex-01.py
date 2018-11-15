# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны
# любому из чисел в диапазоне от 2 до 9.

array = [i for i in range(2, 100)]

# Итоговое решение))
for i in range(2, 10):
    count = 0
    for j in array:
        if j % i == 0:
            count += 1
    print(f"Кратно {i} - {count} чисел")


# Сначала попробовал это способы, но как-то не по программистски получилось
print(f"кратно 2 {len([i for i in array if i % 2 == 0])}")
print(f"кратно 3 {len([i for i in array if i % 3 == 0])}")
print(f"кратно 4 {len([i for i in array if i % 4 == 0])}")
print(f"кратно 5 {len([i for i in array if i % 5 == 0])}")
print(f"кратно 6 {len([i for i in array if i % 6 == 0])}")
print(f"кратно 7 {len([i for i in array if i % 7 == 0])}")
print(f"кратно 8 {len([i for i in array if i % 8 == 0])}")
print(f"кратно 9 {len([i for i in array if i % 9 == 0])}")


arr_2 = [i for i in array if i % 2 == 0]
arr_3 = [i for i in array if i % 3 == 0]
arr_4 = [i for i in array if i % 4 == 0]
arr_5 = [i for i in array if i % 5 == 0]
arr_6 = [i for i in array if i % 6 == 0]
arr_7 = [i for i in array if i % 7 == 0]
arr_8 = [i for i in array if i % 8 == 0]
arr_9 = [i for i in array if i % 9 == 0]

print(array)
print(f"Кратно 2 {len(arr_2)}")
print(f"Кратно 3 {len(arr_3)}")
print(f"Кратно 4 {len(arr_4)}")
print(f"Кратно 5 {len(arr_5)}")
print(f"Кратно 6 {len(arr_6)}")
print(f"Кратно 7 {len(arr_7)}")
print(f"Кратно 8 {len(arr_8)}")
print(f"Кратно 9 {len(arr_9)}")
