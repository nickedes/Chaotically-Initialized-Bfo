def logistic(x, a=0.4):
    x = a*x*(1-x)
    return x

x, y = 0.3, 0.4
for num in range(100):
    x = logistic(x)
    y = logistic(y)
    print(x, ",", y)
