from math import floor as f


def gauss(x):
    if x == 0:
        return 0
    else:
        return 1/x - f(1/x)

x = [0.3, 0.8, 0.17]
for y in x:
    temp = y
    for num in range(100):
    temp = gauss(temp)
    print(temp)
