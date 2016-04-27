from init import *
from optimization import *
from json import dumps

num = 10  # number of Chaotic maps

if __name__ == '__main__':
    print("Bacterial Foraging Optimization Algorithm")
    print("Dimension: ", dimension)
    # For tracking global minima. ;)
    results = {'c_space': c_space, 'c_prob': c_prob, 'c_tumble': c_tumble}
    res = {}
    for i in range(num):
        best = INF                 # the best solution found during the search
        fe_count = 0               # number of objective function evaluations
        # search space [-100, 100]^dimension
        c_tumble, c_space, c_prob, space = initialize_space(
            space, -100.0, 100.0)
        # random initialization within the search space
        population, c_space, fe_count, best = initialize_population(
            i+1, population, c_space, fe_count, best)
        # minimization of objective function
        best, iteration_values = optimization(
            i+1, population, c_space, fe_count, best, c_prob, c_tumble)
        if best == 0.0:
            results[str(i+1)] = 1.0
        else:
            results[str(i+1)] = best
            res[str(i+1)] = iteration_values

    # with open('data.py', 'a') as f:
    #     f.write(dumps(results, sort_keys=True) + '\n')

    with open('data_graphs.py', 'a') as f:
        f.write(dumps(res, sort_keys=True) + '\n')
    print("Updated!")
