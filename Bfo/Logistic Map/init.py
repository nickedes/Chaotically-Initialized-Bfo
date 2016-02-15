"""Initializations."""
# from random import random
from fitness import objective_function
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
N_ed = 4      # number of elimination-dispersal events
N_re = 10       # number of reproduction steps
N_ch = 20      # number of chemotactic steps
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
c_space = 0.2   # chaotic init for space
c_prob = 0.4   # chaotic init for probability


def logistic(x, a=0.4):
    x = a*x*(1-x)
    return x


# def random_val(a, b):
#     num = random()
#     num = a + num*(b-a)
#     return num


# def objective_function(x, fe_count, best):

#     rez = 0.0
#     fe_count = fe_count + 1
#     # Sphere Function
#     for i in range(dimension):
#         rez += pow(x.vect[i], 2.0)

#     x.cost = rez

#     if x.cost < best:
#         best = x.cost
#     return x, fe_count, best


def initialize_space(space, a, b):
    """
    set the bounds values for search space.
    """
    for i in range(dimension):
        space[i][0] = a
        space[i][1] = b
    return c_space, c_prob, space


def initialize_population(num, population, c_space, fe_count, best):
    """
    Distribute the population within the search space.
    """
    for i in range(S):
        # randomly distribute the initial population
        for j in range(dimension):
            c_space = logistic(c_space)
            population[i].vect[j] = c_space
        # TODO : implent fitness function
        population[i], fe_count, best = objective_function(
            num, population[i], fe_count, best)
        population[i].fitness = 0.0
        population[i].health = 0.0
        population[i].step_size = ss
    return population, c_space, fe_count, best
