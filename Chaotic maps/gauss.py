from math import floor as f


def gauss(x):
    if x == 0:
        return 0
    else:
        return 1/x - f(1/x)

print(gauss(1.2))
