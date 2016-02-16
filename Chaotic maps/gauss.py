from math import floor as f


def gauss(x):
    if x == 0:
        return 0
    else:
        return 1/x - f(1/x)

x = 0.17
for num in range(100):
    x = gauss(x)
    print(x)
