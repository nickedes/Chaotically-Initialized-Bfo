def piecewise(x, p=0.4):
    if 0 <= x < p:
        return x/p
    elif p <= x < 0.5:
        return (x-p)/(0.5-p)
    elif 0.5 <= x < 1-p:
        return (1-p-x)/(0.5-p)
    elif 1-p <= x < 1:
        return (1-x)/p
    else:
        print(x)
        raise ValueError

# check!
x = 0.3
for num in range(100):
    x = piecewise(x)
    print(x)

