def tent(x, a=0.7):
    if x < a:
        return x/a
    elif x >= a:
        return (1-x)/(1-a)

x = 0.1
for num in range(100):
    x = tent(x)
    print(x)
