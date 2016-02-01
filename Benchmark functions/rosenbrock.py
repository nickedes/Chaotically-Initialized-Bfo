# ROSENBROCK FUNCTION
# Input Domain: [-2.048, 2.048]
from sphere import normalization

def rosenbrock(x):
	result = 0
	for i in range(len(x)):
		result += 100*(x[i+1]-x[i]**2)**2 + (x[i] - 1)**2
	return result
