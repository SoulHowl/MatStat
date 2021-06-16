
from numpy.random import rand

from math import *
plotdots = 10**4


a, b = -3, 3
def phi(x): return fabs(x)


L, R = 0, 3


def X():
    return a + (b - a) * rand()


def Y():
    return phi(X())

def f(y):
    if 0 < y < 3:
        return 1/3
    return 0


def F(y):
    if y <= 0:
        return 0
    if 0 <= y < 3:
        return (1/3) * y
    if 3 <= y:
        return 1
    raise ValueError


