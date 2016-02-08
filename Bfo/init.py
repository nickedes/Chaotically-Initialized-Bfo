"""Initializations."""
from math import pi

INF = float("inf")
dimension = 10
S = 50      # population size
Sr = S/2     # number to split
ss = 0.6     # step size
N_ed = 3       # number of elimination-dispersal events
N_re = 6       # number of reproduction steps
N_ch = 20      # number of chemotactic steps
N_sl = 4       # swim length
p_ed = 0.25    # eliminate probability
d_attr = 0.1     # depth of the attractant
w_attr = 0.2     # width of the attractant signal
h_rep = d_attr  # height of the repellant effect
w_rep = 10.0    # width of the repellant
