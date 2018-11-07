# Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках домашнего задания первых трех уроков.

# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

# import timeit
import cProfile

#n = 10


def foo(n):
    if n == 1:
        return 1
    return foo(n - 1) * (-0.5) + 1


# cProfile.run('foo(10)')     10/1    0.000    0.000    0.000    0.000 ex_01.py:13(foo)
# cProfile.run('foo(100)')    100/1    0.000    0.000    0.000    0.000 ex_01.py:13(foo)
# cProfile.run('foo(300)')    300/1    0.001    0.000    0.001    0.001 ex_01.py:13(foo)

# "ex_01.foo(10)"
# 1000 loops, best of 5: 1.9 usec per loop
# "ex_01.foo(20)"
# 1000 loops, best of 5: 3.9 usec per loop
# "ex_01.foo(100)"
# 1000 loops, best of 5: 19.8 usec per loop

#
# def f(n):
#     item = 1
#     summ = 0
#     for _ in range(n):
#         summ += item
#         item /= -2
#     return summ

# "ex_01.f(10)"
# 1000 loops, best of 5: 1.24 usec per loop
# "ex_01.f(20)"
# 1000 loops, best of 5: 2.01 usec per loop
# "ex_01.f(100)"
# 1000 loops, best of 5: 7.96 usec per loop


# cProfile.run('f(10)')        1    0.000    0.000    0.000    0.000 ex_01.py:26(f)
# cProfile.run('f(100)')        1    0.000    0.000    0.000    0.000 ex_01.py:26(f)
# cProfile.run('f(10000)')        1    0.001    0.001    0.001    0.001 ex_01.py:26(f)

