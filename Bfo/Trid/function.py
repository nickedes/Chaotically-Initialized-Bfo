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
