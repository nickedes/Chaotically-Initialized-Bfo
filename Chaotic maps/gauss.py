from math import floor as f


def gauss(x):
    if x == 0:
        return 0
    elif 0 < x < 1:
        return 1/x - f(1/x)
