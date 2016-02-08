from init import *
from optimization import *

if __name__ == '__main__':
    print("Bacterial Foraging Optimization Algorithm")
    print("Dimension: ", dimension)
    best = INF                 # the best solution found during the search
    fe_count = 0               # number of objective function evaluations
    # search space [-100, 100]^dimension
    space = initialize_space(space, -100.0, 100.0)
    # random initialization within the search space
    population, fe_count, best = initialize_population(
        population, space, fe_count, best)
    # minimization of objective function
    optimization(population, space, fe_count, best)
