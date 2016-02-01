# SCHWEFEL FUNCTION
# Input Domain: [-65.536, 64.536]
from sphere import normalization
from math import sin,sqrt
x_min, x_max = -65.536, 64.536
def schwefel(x):
    x = normalization(x, x_min, x_max)
    result = 0
    for elem in x:
        result += (-1*elem)*sin(sqrt(abs(elem)))
    return result
