# Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования Решета Эратосфена;
# Использовать алгоритм решето Эратосфена

import cProfile


def simple(n):
    lst = [2]
    i = 2
    while len(lst) < n:
        i += 1
        for j in lst:
            if i % j == 0:
                break
        else:
            lst.append(i)

    return lst[n - 1]


# cProfile.run('simple(10)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 ex_02.py:8(simple)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        28    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         9    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#


# cProfile.run('simple(100)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 ex_02.py:8(simple)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#       540    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        99    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# cProfile.run('simple(200)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#         1    0.002    0.002    0.002    0.002 ex_02.py:8(simple)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#      1222    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       199    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



# "ex_02.simple(10)"
# 1000 loops, best of 5: 11.7 usec per loop
# "ex_02.simple(100)"
# 1000 loops, best of 5: 431 usec per loop
# "ex_02.simple(200)"
# 1000 loops, best of 5: 1.54 msec per loop





