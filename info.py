import numpy as np
from numpy.random import rand, normal
#from scipy.stats import norm
from math import *
plotdots = 10**4



## Y = x^2 при x равнораспределённом на [-1..2]

a, b = -3, 3
def phi(x): return fabs(x)
L, R = 0, 4

def X(): return a + (b - a) * rand()
def Y(): return phi(X())

def f(y):
    if 0 < y < 1: return 1 / (3 * y**0.5)
    if 1 <= y < 4: return 1 / (6 * y**0.5)
    return 0

def F(y):
    if y <= 0: return 0
    if 0 <= y < 1: return (2/3) * y**0.5
    if 1 <= y < 4: return 1/3 + (1/3) * y**0.5
    if 4 <= y: return 1
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



## Вариант 7: Y = 1/(1+x) при x равнораспределённом на [a..b]

# a, b = -6, -2
# def phi(x): return 1/(1+x) 
# L, R = phi(b), phi(a)

# def X(): return a + (b - a) * rand()
# def Y(): return phi(X())

# def f(y):
    # if -1 < y < -1/5: return (1/4) * abs(-1/y + (y-1)/y**2)
    # return 0

# def F(y):
    # if y <= -1: return 0
    # if -1 <= y < -1/5: return -1/(4*y) - 1/4
    # if -1/5 <= y: return 1
    # raise ValueError



## Вариант 15: Y имеет дискретные точки

# eps = np.nextafter(0, +np.inf)
# a, b = -5, 5

# def phi(x):
    # if x < -1: return -2
    # if -1 <= x <= 1: return 2*x
    # if x > 1: return 2
    # raise ValueError

# L, R = -2, 2

# def X(): return a + (b - a) * rand()
# def Y(): return phi(X())

# def f(y):
    # if y == -2: return np.inf
    # if -2 < y < 2: return 1/20
    # if y == 2: return np.inf
    # return 0

# def F(y):
    # if y < -2: return 0
    # if y == -2: return (-1-a) / (b-a)
    # if -2 < y < 2: return F(-2) + (y+2) * 1/20
    # if y == 2: return F(-2-eps) + (b-1) / (b-a)
    # if 2 <= y: return 1
    # print(y)
    # raise ValueError

