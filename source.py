import numpy as np
import matplotlib.pyplot as plt
from lattice import *
from metropolis_hastings import *

#The Ising model of ferromagnetism focuses on interactions of spin sites in a lattice, where each site can have a "spin"
#  of one of two values: -1 or 1. The interaction between adjacent sites is encoded by a value J, where J>0 describes a ferromagnetic
#  interaction, J<0 encodes an antiferromagnetic interaction between lattice sites, and J=0 implies that the spins on each site are 
#  non-interacting.

lattice1 = Lattice(100, 0)
times = [1000, 10000]
evolve_and_plot(lattice1, times, 100, 100)






