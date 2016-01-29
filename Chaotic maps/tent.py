def tent(x):
	if x < 0.7:
		return x/0.7
	elif x >= 0.7:
		return 10*(1-x)/3
