from init import *
from optimization import *
from json import dumps
from limit import achieved

num = 9  # number of fitness functions

if __name__ == '__main__':
    print("Bacterial Foraging Optimization Algorithm")
    print("Dimension: ", dimension)
    # For tracking global minima. ;)
    results = {}
    for i in range(num):
        best = INF                 # the best solution found during the search
        fe_count = 0               # number of objective function evaluations
        # search space [-100, 100]^dimension
        space = initialize_space(space, -100.0, 100.0)
        # random initialization within the search space
        population, fe_count, best = initialize_population(
            i+1, population, space, fe_count, best)
        # minimization of objective function
        best = optimization(i+1, population, space, fe_count, best)
        results[str(i+1)] = best

    for x in results:
        if results[x] > achieved[x]:
            results[x] = achieved[x]
    if results != achieved:
        with open('data.py', 'a') as f:
            f.write(dumps(results) + '\n')
