from init import *
from optimization import *

if __name__ == '__main__':
    print("Bacterial Foraging Optimization Algorithm")
    print("Dimension: ", dimension)
    # search space [-100, 100]^dimension
    space = initialize_space(space, -100.0, 100.0)
    # random initialization within the search space
    population = initialize_population(population, space)
    # minimization of objective function
    optimization(population, space)
