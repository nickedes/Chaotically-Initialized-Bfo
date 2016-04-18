from init import *
from optimization import *
from json import dumps

num = 10  # number of fitness functions

if __name__ == '__main__':
    print("Bacterial Foraging Optimization Algorithm")
    print("Dimension: ", dimension)
    # For tracking global minima. ;)
    func_dict = {
        1: "sphere",
        2: "rastrigin",
        3: "rosenbrock",
        4: "schwefel",
        5: "quartic",
        6: "ackley",
        7: "schaffer",
        8: "griewank",
        9: "matyas",
        10: "trid"
    }
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
        if best == 0.0:
            results[str(i+1)] = 1.0
        else:
            results[str(i+1)] = best

    with open('data.py', 'a') as f:
        f.write(dumps(results, sort_keys=True) + '\n')
    print("Updated!")
