"""Fitness Functions."""
from math import *


def normalization(x, x_min=-5.12, x_max=5.12):
    """
    For normalization of data within specified Input Domain.
    """
    for i in range(len(x.vect)):
        x.vect[i] = x_min + x.vect[i]*(x_max-x_min)
    return x


def sphere(x, fe_count, best):
    """
    SPHERE FUNCTION
    Input Domain: [-5.12, 5.12]
    """
    # x = normalization(x)
    rez = 0.0
    fe_count = fe_count + 1
    for i in range(len(x.vect)):
        rez += pow(x.vect[i], 2.0)

    x.cost = rez

    if x.cost < best and x.cost != 0.0:
        best = x.cost
    return x, fe_count, best


def rastrigin(x, fe_count, best):
    """
    RASTRIGIN FUNCTION
    Input Domain: [-5.12, 5.12]
    """
    # x = normalization(x)
    result = 0
    fe_count = fe_count + 1
    for i in range(len(x.vect)):
        result += x.vect[i]**2 - 10*cos(2*pi*x.vect[i]) + 10

    x.cost = result
    if x.cost < best and x.cost != 0.0:
        best = x.cost
    return x, fe_count, best


def rosenbrock(x, fe_count, best):
    """
    ROSENBROCK FUNCTION
    Input Domain: [-2.048, 2.048]
    """
    # x_min, x_max = -2.048, 2.048
    # x = normalization(x, x_min, x_max)
    result = 0
    fe_count = fe_count + 1
    for i in range(len(x.vect)-1):
        result += 100*(x.vect[i+1]-x.vect[i]**2)**2 + (x.vect[i] - 1)**2

    x.cost = result
    if x.cost < best and x.cost != 0.0:
        best = x.cost
    return x, fe_count, best


def schwefel(x, fe_count, best):
    """
    SCHWEFEL FUNCTION
    Input Domain: [-65.536, 64.536]
    """
    # x = normalization(x, x_min, x_max)
    result = 0
    fe_count = fe_count + 1
    for i in range(len(x.vect)-1):
        result += (-1*x.vect[i])*sin(sqrt(abs(x.vect[i])))

    x.cost = result
    if abs(x.cost) < abs(best) and x.cost != 0.0:
        best = abs(x.cost)
    return x, fe_count, best


def quartic(x, fe_count, best):
    """
    QUARTIC FUNCTION
    Input Domain: [-1.28, 1.28]
    """
    x = normalization(x, -1.28, 1.28)
    result = 0
    fe_count = fe_count + 1
    for i in range(1, len(x.vect)-1):
        result += (i+1)*pow(x.vect[i], 4)
    result += x.vect[0]

    x.cost = result
    if abs(x.cost) < abs(best) and x.cost != 0.0:
        best = abs(x.cost)
    return x, fe_count, best


def ackley(x, fe_count, best):
    # x = normalization(x, -50, 50)
    fe_count = fe_count + 1
    sum_sq = 0.0
    sum_cos = 0.0
    for i in range(len(x.vect)):
        sum_sq += pow(x.vect[i], 2)
        sum_cos += cos(2*pi*x.vect[i])
    sum_sq = (-0.2)*sqrt(sum_sq/len(x.vect))
    sum_cos = sum_cos/len(x.vect)
    x.cost = (-20)*exp(sum_sq) - exp(sum_cos) + 20 + e
    if abs(x.cost) < abs(best) and x.cost != 0.0:
        best = abs(x.cost)
    return x, fe_count, best


def f5(x, fe_count, best):
    result = 0.0
    for i in range(len(x.vect)):
        result += abs(x.vect[i]) - 10*cos(sqrt(abs(10*x.vect[i])))
    x.cost = result
    if abs(x.cost) < abs(best) and x.cost != 0.0:
        best = abs(x.cost)
    return x, fe_count, best


def griewank(x, fe_count, best):
    result = 0.0
    sum_sq = pow(x.vect[0], 2.0)
    prod_cos = cos(x.vect[0])
    fe_count = fe_count + 1
    for i in range(1, len(x.vect)):
        sum_sq += pow(x.vect[i], 2.0)
        prod_cos *= cos(x.vect[i]/sqrt(i+1))
    result = sum_sq/4000 - prod_cos + 1
    x.cost = result
    if abs(x.cost) < abs(best) and x.cost != 0.0:
        best = abs(x.cost)
    return x, fe_count, best


def matyas(x, fe_count, best):
    """
    https://en.wikipedia.org/wiki/Test_functions_for_optimization
    """
    sum_sq, prod_term = 0.0, 1.0
    fe_count = fe_count + 1
    for i in range(len(x.vect)):
        sum_sq += pow(x.vect[i], 2.0)
        prod_term *= x.vect[i]

    x.cost = 0.26*sum_sq - 0.48*prod_term

    if abs(x.cost) < abs(best) and x.cost != 0.0:
        best = x.cost
    return x, fe_count, best


def objective_function(num, x, fe_count, best):
    """
    To use Fitness functions based on value of 'num'.
    """
    if num == 1:
        return sphere(x, fe_count, best)
    elif num == 2:
        return rastrigin(x, fe_count, best)
    elif num == 3:
        return rosenbrock(x, fe_count, best)
    elif num == 4:
        return schwefel(x, fe_count, best)
    elif num == 5:
        return quartic(x, fe_count, best)
    elif num == 6:
        return ackley(x, fe_count, best)
    elif num == 7:
        return schaffer(x, fe_count, best)
    elif num == 8:
        return griewank(x, fe_count, best)
    elif num == 9:
        return matyas(x, fe_count, best)
    elif num == 10:
        return trid(x, fe_count, best)
    else:
        pass
