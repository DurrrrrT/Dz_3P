# Вычислить число Пи c заданной точностью d
# Пример: при d = 0.001,  c= 3.141.

import math


def pi(d):
    k = 1
    x = 0
    while abs(math.pi - x) > d:
        x = x+4*((-1)**(k+1))/(2*k-1)
        k += 1
    return x


precision = 0.001
print(math.pi)
print(pi(precision))

