"""Initializations."""
# from random import random
# from fitness import objective_function
from maps import map_func
import sys
INF = sys.maxsize
dimension = 2


class Cell:
    vect = [0]*dimension      # position in search space
    cost = 0.0                # objective function value
    fitness = 0.0             # cost value and attractant and repellent effects
    health = 0.0              # the health of bacterium
    step_size = 0.0           # step in the search area

S = 20      # population size
Sr = S//2     # number to split
ss = 0.6     # step size
N_ed = 12      # number of elimination-dispersal events
N_re = 10       # number of reproduction steps
N_ch = 10      # number of chemotactic steps
N_sl = 2       # swim length
p_ed = 0.20    # eliminate probability
d_attr = 0.1     # depth of the attractant
w_attr = 0.2     # width of the attractant signal
h_rep = d_attr  # height of the repellant effect
w_rep = 1.0    # width of the repellant

population = [Cell() for i in range(S)]  # population of bacteria

space = [[0]*2]*dimension  # the boundaries of the search space
rand_vect = [0]*dimension  # direction of movement after a tumble
delta = [0]*dimension      # used in the normalization of the rand_vect

# chaotic initializations
c_space = 0.3   # chaotic init for space
c_prob = 0.8   # chaotic init for probability
c_tumble = 0.5  # chaotic init for tumbling


def Trid(x, fe_count, best):
    """
    http://www.sfu.ca/~ssurjano/trid.html
    """
    sum_sq = 0.0
    fe_count = fe_count + 1
    for i in range(len(x.vect)):
        sum_sq += pow(x.vect[i] - 1, 2.0)

    sum_consecutive = 0.0
    for i in range(len(x.vect)-1):
        sum_consecutive += x.vect[i]*x.vect[i+1]
    x.cost = sum_sq - sum_consecutive

    if abs(x.cost) < abs(best) and x.cost != 0.0:
        best = abs(x.cost)
    return x, fe_count, best


def initialize_space(space, a, b):
    """
    set the bounds values for search space.
    """
    for i in range(dimension):
        space[i][0] = a
        space[i][1] = b
    return c_tumble, c_space, c_prob, space


def initialize_population(num, population, c_space, fe_count, best):
    """
    Distribute the population within the search space.
    """
    for i in range(S):
        # randomly distribute the initial population
        for j in range(dimension):
            c_space = map_func(num, c_space, i+j+1)
            population[i].vect[j] = c_space
        # TODO : implent fitness function
        population[i], fe_count, best = sphere(population[i], fe_count, best)
        population[i].fitness = 0.0
        population[i].health = 0.0
        population[i].step_size = ss
    return population, c_space, fe_count, best
