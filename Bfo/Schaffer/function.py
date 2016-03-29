def Schaffer(x, fe_count, best):
    """
    https://en.wikipedia.org/wiki/Test_functions_for_optimization
    Name - Schaffer function N. 2
    """
    sum_sq = 0.0
    fe_count = fe_count + 1
    for i in range(len(x.vect)):
        sum_sq += pow(x.vect[i], 2.0)

    x.cost = 0.5 + (pow(sin(sum_sq), 2.0) - 0.5)/pow((1 + 0.001*sum_sq), 2.0)

    if abs(x.cost) < abs(best) and x.cost != 0.0:
        best = abs(x.cost)
    return x, fe_count, best
