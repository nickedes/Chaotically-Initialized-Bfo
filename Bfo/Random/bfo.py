from init import *
from optimization import *

num = 6  # number of fitness functions

if __name__ == '__main__':
    print("Bacterial Foraging Optimization Algorithm")
    print("Dimension: ", dimension)
    for i in range(num):
        best = INF                 # the best solution found during the search
        fe_count = 0               # number of objective function evaluations
        # search space [-100, 100]^dimension
        c_space, space = initialize_space(c_space, space, -100.0, 100.0)
        # random initialization within the search space
        population, c_space, fe_count, best = initialize_population(
            i+1, population, c_space, fe_count, best)
        # minimization of objective function
        optimization(i+1, population, c_space, fe_count, best)
