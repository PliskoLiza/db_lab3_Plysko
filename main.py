import math
from math import pi


def integral(x_0, x_n, h, f, i=0):
    if x_0 + h > x_n:
        return i
    else:
        i += h * f(x_0)
        return integral(x_0 + h, x_n, h, f, i)


interval = [-pi/6, pi/2]
h = 0.007247

print(integral(interval[0], interval[1], h,
               lambda x : math.sin(1 + math.pow(math.cos(x), 2))))