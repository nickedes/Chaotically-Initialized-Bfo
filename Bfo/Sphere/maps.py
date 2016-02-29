from math import *


def logistic(x, a=0.4):
    x = a*x*(1-x)
    return x


def gauss(x):
    if x == 0:
        x = 1
    else:
        x = 1/x - floor(1/x)
    return x


def piecewise(x, p=0.4):
    if 0 <= x < p:
        x = x/p
    elif p <= x < 0.5:
        x = (x-p)/(0.5-p)
    elif 0.5 <= x < 1-p:
        x = (1-p-x)/(0.5-p)
    elif 1-p <= x < 1:
        x = (1-x)/p
    return x


def singer(x, u=1.07):
    if 0 < x < 1:
        x = u*(7.86*x - 23.31*x**2 + 28.75*x**3 - 13.302875*x**4)
        return x


def tent(x, a=0.7):
    if x < a:
        x = x/a
    elif x >= a:
        x = (1-x)/(1-a)
    return x


def iterative(x, a=0.7):
    x = sin(a*pi/x)
    return x


def sine(x, a=4):
    x = (a/4)*sin(pi*x)
    return x


def circle(x, a=0.5, b=0.2):
    y = x + b - (a/(2*pi))*sin(2*pi*x)
    return y % 1


def sinusoidal(x, a=2.3):
    x = a*pow(x, 2)*sin(pi*x)
    return x


def chebyshev(x, iteration_num):
    x = cos(iteration_num*acos(x))
    return x


def map_func(num, x, iteration_num):
    """
    To use Chaotic maps functions based on value of 'num'.
    """
    if num == 1:
        return logistic(x)
    elif num == 2:
        return gauss(x)
    elif num == 3:
        return piecewise(x)
    elif num == 4:
        return singer(x)
    elif num == 5:
        return tent(x)
    elif num == 6:
        return iterative(x)
    elif num == 7:
        return sine(x)
    elif num == 8:
        return circle(x)
    elif num == 9:
        return sinusoidal(x)
    elif num == 10:
        return chebyshev(x, iteration_num)
