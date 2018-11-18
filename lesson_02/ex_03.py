# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр
# и вывести на экран. Например, если введено число 3486, то надо вывести число 6843.

num1 = int(input("Введите число! "))
num = num1
revers_number = 0
while num % 10 != 0:
    digit = num % 10
    num = num // 10
    revers_number = revers_number * 10 + digit

print(f"{num1} - Начальное число  \n{revers_number} - Реверсированное число ")
