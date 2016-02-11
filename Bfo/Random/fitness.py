"""Fitness Functions."""


def normalization(x, x_min=-5.12, x_max=5.12):
    """
    For normalization of data within specified Input Domain.
    """
    for i in range(dimension):
        x.vect[i] = x_min + x.vect[i]*(x_max-x_min)
    return x


def sphere(x, fe_count, best):
    """
    SPHERE FUNCTION
    Input Domain: [-5.12, 5.12]
    """
    x = normalization(x)
    rez = 0.0
    fe_count = fe_count + 1
    for i in range(dimension):
        rez += pow(x.vect[i], 2.0)

    x.cost = rez

    if x.cost < best:
        best = x.cost
    return x, fe_count, best
