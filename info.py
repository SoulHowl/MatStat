import numpy as np
from numpy.random import rand, normal
#from scipy.stats import norm
from math import *
plotdots = 10**4


# Y = |x| при x равнораспределённом на [-3..3]
a, b = -3, 3
def phi(x): return fabs(x)


L, R = 0, 3


def X():
    return a + (b - a) * rand()


def Y():
    return phi(X())

def f(y):
    #if 0 < y < 1: return 1 / (3 * y**0.5)
    #if 1 <= y < 4: return 1 / (6 * y**0.5)
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



## Случайное число равнораспределённое на отрезке [0..1]

# a, b = 0, 1
# def phi(x): return x
# L, R = 0, 1

# def X(): return a + (b - a) * rand()
# def Y(): return phi(X())

# def f(y):
    # if 0 < y < 1: return 1
    # return 0

# def F(y):
    # if y <= 0: return 0
    # if 0 <= y < 1: return y
    # if 1 <= y: return 1
    # raise ValueError



## Нормальное распределение с M = 0 и sigma = 1

# mu, sigma = 0, 1
# a, b = 0, 1
# def phi(x): return x
# L, R = -5, 5

# def X(): return normal(mu, sigma)
# def Y(): return phi(X())

# def f(y):
    # return norm.pdf(y, mu, sigma)

# def F(y):
    # return norm.cdf(y, mu, sigma)

