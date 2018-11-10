# . Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’].
# Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

first_num = list(input("Введите число в шестнадцатиричном формате"))
second_num = list(input("Введите число в шестнадцатиричном формате"))
dict_16_to_10 = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                 '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

dict_10_to_16 = {v: k for k, v in dict_16_to_10.items()}

first_num_10 = []
second_num_10 = []

for i in first_num:
    first_num_10.append(dict_16_to_10[i])
for i in second_num:
    second_num_10.append(dict_16_to_10[i])

print(first_num_10)
print(second_num_10)


first_10 = 0
second_10 = 0

for i in range(len(first_num_10)):
    first_10 = first_10 + first_num_10[i] * (16 ** (len(first_num_10) - 1 - i))

for i in range(len(second_num_10)):
    second_10 = second_10 + second_num_10[i] * (16 ** (len(second_num_10) - 1 - i))

print(first_10)
print(second_10)

summ = first_10 + second_10
mult = first_10 * second_10
print(summ)
print(mult)


def convert_10_to_16(num):
    num_16 = []
    while num > 0:
        num_16.append(dict_10_to_16[num % 16])
        num = num // 16

    num_16.reverse()
    return num_16


summ_16 = convert_10_to_16(summ)
mult_16 = convert_10_to_16(mult)

print(summ_16)
print(mult_16)