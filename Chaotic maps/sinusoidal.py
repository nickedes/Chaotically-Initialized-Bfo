from math import *
from decimal import Decimal as d


def sinusoidal(x, a=2.3):
    x = a*pow(x, 2)*sin(pi*x)
    if x == 0:
        return 1
    return x


x = [0.3, 0.8, 0.17]
for y in x:
    temp = y
    for num in range(100):
        temp = d(sinusoidal(float(temp)))
        print(temp)
    print("____")
