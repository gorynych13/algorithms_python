# Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках домашнего задания первых трех уроков.

# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

# import timeit
# import cProfile

#n = 10


def foo(n):
    if n == 1:
        return 1
    return foo(n - 1) * (-0.5) + 1


# def f(n):
#     item = 1
#     summ = 0
#     for _ in range(n):
#         summ += item
#         item /= -2
#     return summ



