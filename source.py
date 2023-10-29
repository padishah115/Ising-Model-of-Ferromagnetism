import numpy as np
import matplotlib.pyplot as plt

#The Ising model of ferromagnetism focuses on interactions of spin sites in a lattice, where each site can have a "spin"
#  of one of two values: -1 or 1. The interaction between adjacent sites is encoded by a value J, where J>0 describes a ferromagnetic
#  interaction, J<0 encodes an antiferromagnetic interaction between lattice sites, and J=0 implies that the spins on each site are 
#  non-interacting.

def init_lattice(width, type):
    """Type 1: a lattice where all of the spins are spin-up. 
    Type 0: Spins are randomly assigned values of +1 or -1.
    Type -1: we have a lattice where all of the spins are spin-down."""

    if type == 0:
        lattice = np.random.randint((0,2), size = (width, width), dtype = int) - np.ones()

    if type == 1:
        lattice = np.ones((width, width), dtype = int)

    if type == -1:
        lattice = -1*np.ones((width, width), dtype = int)

    return lattice