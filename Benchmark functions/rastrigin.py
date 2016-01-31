# RASTRIGIN FUNCTION
# Input Domain: [-5.12, 5.12]
from math import cos, pi
from sphere import normalization


def rastrigin(x):
    x = normalization(x)
    result = 0
    for elem in x:
        result += elem**2 - 10*cos(2*pi*elem) + 10
    return result
