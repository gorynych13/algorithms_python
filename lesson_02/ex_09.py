# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.
max_num = 0
dig_sum = 0


def digit_sum(num):
    if num < 10:
        return num
    else:
        return num % 10 + digit_sum(num // 10)


while True:
    num = int(input("Введите целое число\nЧтобы закончить введите 0"))
    if num == 0:
        break
    if dig_sum < digit_sum(num):
        max_num = num
        dig_sum = digit_sum(num)

print(f"Максимальная сумма {dig_sum} у числа{max_num}")

