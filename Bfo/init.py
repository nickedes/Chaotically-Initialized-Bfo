"""Initializations."""
from random import randint

INF = float("inf")
dimension = 10


class Cell:
    vect = [0]*dimension      # position in search space
    cost = 0.0                # objective function value
    fitness = 0.0             # cost value and attractant and repellent effects
    health = 0.0              # the health of bacterium
    step_size = 0.0           # step in the search area

S = 50      # population size
Sr = S/2     # number to split
ss = 0.6     # step size
N_ed = 3       # number of elimination-dispersal events
N_re = 6       # number of reproduction steps
N_ch = 20      # number of chemotactic steps
N_sl = 4       # swim length
p_ed = 0.25    # eliminate probability
d_attr = 0.1     # depth of the attractant
w_attr = 0.2     # width of the attractant signal
h_rep = d_attr  # height of the repellant effect
w_rep = 10.0    # width of the repellant

population = [Cell() for i in range(S)]  # population of bacteria

space = [[0]*2]*dimension  # the boundaries of the search space
rand_vect = [0]*dimension  # direction of movement after a tumble
delta = [0]*dimension      # used in the normalization of the rand_vect

best = INF                 # the best solution found during the search
fe_count = 0               # number of objective function evaluations


def initialize_space(a, b):
    """
    set the bounds values for search space.
    """
    for i in range(dimension):
        space[i][0] = a
        space[i][1] = b


def initialize_population():
    """
    Distribute the population within the search space.
    """
    for i in range(S):
        # randomly distribute the initial population
        for j in range(dimension):
            population[i].vect[j] = randint(space[j][0], space[j][1])
        # TODO : implent fitness function
        # objective_function(population[i])
        population[i].fitness = 0.0
        population[i].health = 0.0
        population[i].step_size = ss
