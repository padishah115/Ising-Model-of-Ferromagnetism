import numpy as np
import matplotlib.pyplot as plt
from lattice import *

#The Ising model of ferromagnetism focuses on interactions of spin sites in a lattice, where each site can have a "spin"
#  of one of two values: -1 or 1. The interaction between adjacent sites is encoded by a value J, where J>0 describes a ferromagnetic
#  interaction, J<0 encodes an antiferromagnetic interaction between lattice sites, and J=0 implies that the spins on each site are 
#  non-interacting.


def neighboring_sites_sum(i, j, lattice):
    """Sums the spins on all neighbouring sites as per the prescription of the ising model. Takes into account periodic boundary conditions
    by "wrapping around" the lattice for cases on the edge of the lattice. Doesn't involve diagonally adjacent lattice sites."""

    neighbor_sum = 0
    width = lattice.get_width()

    if i == 0 and j == 0:
        """Top left corner"""
        neighbor_sum = lattice[0,1] + lattice [1,0] + lattice[0, width-1] + lattice [width-1, 0]

    if i == width -1 and j == 0:
        """Top right corner"""
        neighbor_sum = lattice[i-1, j] + lattice[i, j+1] + lattice[i, width-1] + lattice[0,0]

    if i == width -1 and j == width-1:
        """Bottom right corner"""
        neighbor_sum = lattice[width-1, 0] + lattice[i, j-1] + lattice[0, j] + lattice[i-1, j]

    if i == 0 and j == width-1:
        """Bottom left corner"""
        neighbor_sum = lattice[0,0] + lattice[i+1, j] + lattice[width-1, j] + lattice[i, j-1]

    if i == 0 and j != 0: 
        """Far left column"""
        neighbor_sum = lattice[i, j-1] + lattice[i, j+1] + lattice[i+1, j] + lattice[width-1, j]

    if i == width-1 and j != 0:
        """Far right column"""
        neighbor_sum = lattice[i, j+1] + lattice[i, j+1] + lattice[i-1, j] + lattice[0, j]

    if i != 0 and j == 0:
        """Top row"""
        neighbor_sum = lattice[i+1, j] + lattice[i-1,j] + lattice[i, j+1] + lattice[i, width-1]

    if i != 0 and j == width-1:
        """Bottom row"""
        neighbor_sum = lattice[i+1, j] + lattice[i-1, j] + lattice[i, j-1] + lattice[i, 0]

    else:
        neighbor_sum = lattice[i+1, j] + lattice [i-1, j] + lattice[i, j+1] + lattice[i, j-1]

    return neighbor_sum


lattice1 = Lattice(5, 0)

lattice1.plot_lattice()


