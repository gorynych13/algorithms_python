# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа
# не должна завершаться, а должна запрашивать новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
# сообщать ему об ошибке и снова запрашивать знак операции. Также сообщать пользователю о
# невозможности деления на ноль, если он ввел 0 в качестве делителя.

while True:
    operation = input("Введите название операции (0-выход, +, -, *, /) ")
    if operation == '0':
        print("Программа завершена!")
        break
    elif operation != '+' and operation != '-' and operation != '*' and operation != '/':
        print("Неправильная команда!!")
        continue
    else:
        number_1 = int(input("Введите первое число: "))
        number_2 = int(input("Введите второе число: "))

        if operation == '+':
            print(f"Сумма числа {number_1} и  {number_2} равна {number_1 + number_2}")
        elif operation == '-':
            print(f"Разность числа {number_1} и  {number_2} равна {number_1 - number_2}")
        elif operation == '*':
            print(f"Произведение числа {number_1} и  {number_2} равна {number_1 * number_2}")
        elif operation == '/':
            if number_2 == 0:
                print("На ноль делить нельзя!")
            else:
                print(f"{number_1 / number_2}")
        else:
            print(f"Неправильная команда: {operation}")





