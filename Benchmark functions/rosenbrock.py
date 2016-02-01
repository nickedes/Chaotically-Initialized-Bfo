# ROSENBROCK FUNCTION
# Input Domain: [-2.048, 2.048]
from sphere import normalization
x_min, x_max = -2.048, 2.048
def rosenbrock(x):
	x = normalization(x, x_min, x_max)
	result = 0
	for i in range(len(x)-1):
		result += 100*(x[i+1]-x[i]**2)**2 + (x[i] - 1)**2
	return result
