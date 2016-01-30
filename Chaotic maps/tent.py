def tent(x, a=0.7):
    if x < a:
        return x/a
    elif x >= a:
        return (1-x)/(1-a)
    else:
        print(x)
        raise ValueError
