"""The Metropolis-Hastings algorithm uses a calculation of the change in energy to the lattice if the value of spin at a given
site changes value. If the energy change is negative, we assume the spin will flip, i.e. that the probability of spin flip is equal to
1. For positive changes to the energy as a result of the flip, we approximate the probability of the spin changing spin using a 
boltzmann factor"""

"""Beta is a parameter encoding the inverse temperature of the system"""

import numpy as np
import matplotlib.pyplot as plt


def get_betaE(lattice, i, j, betaJ, beta):

    #Sum over the neighboring lattice sites
    sum_over_j = lattice.neighboring_sites_sum(i, j)
