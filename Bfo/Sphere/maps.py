def logistic(x, a=0.4):
    x = a*x*(1-x)
    return x


def map_func(num, x):
    """
    To use Chaotic maps functions based on value of 'num'.
    """
    if num == 1:
        return logistic(x)
