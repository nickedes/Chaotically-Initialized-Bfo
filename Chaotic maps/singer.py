def singer(x, u=1.07):
    if 0 < x < 1:
        y = u*(7.86*x - 23.31*x**2 + 28.75*x**3 - 13.302875*x**4)
        return y
    else:
        print(x)
        raise ValueError

x = 0.09
for num in range(100):
    x = singer(x)
    print(x)
