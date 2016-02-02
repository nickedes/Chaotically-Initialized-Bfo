# SPHERE FUNCTION
# Input Domain: [-5.12, 5.12]


def normalization(x, x_min=-5.12, x_max=5.12):
    """
    For normalization of data within specified Input Domain.
    """
    for i in range(len(x)):
        x[i] = (x[i]-x_min)/(x_max-x_min)
    return x


def sphere(x):
    x = normalization(x)
    sum_square = 0
    for elem in x:
        sum_square += elem**2
    return sum_square
