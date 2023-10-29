"""The Metropolis-Hastings algorithm uses a calculation of the change in energy to the lattice if the value of spin at a given
site changes value. If the energy change is negative, we assume the spin will flip, i.e. that the probability of spin flip is equal to
1. For positive changes to the energy as a result of the flip, we approximate the probability of the spin changing spin using a 
boltzmann factor"""

"""Beta is a parameter encoding the inverse temperature of the system"""

import numpy as np
import matplotlib.pyplot as plt
import time


def get_betaE(lattice, i, j, betaJ, betaMuH):
    #Sum over the neighboring lattice sites
    sum_over_j = lattice.neighboring_sites_sum(i, j)

    #Computes the shift in energy as a result of the proposed flip at the given site (i,j)
    beta_deltaE = 2* betaJ * lattice.lattice_grid[i,j] * sum_over_j + betaMuH * lattice.lattice_grid[i,j]

    return beta_deltaE

def try_flip(lattice, betaJ, betaMuH):
    width = lattice.get_width()
    i = np.random.randint(0, width-1)
    j = np.random.randint(0, width-1)

    betadeltaE = get_betaE(lattice, i, j, betaJ, betaMuH)

    if betadeltaE <= 0:
        lattice.lattice_grid[i,j] *= -1

    else:
        probability = np.exp(-1*betadeltaE)
        trial_prob = np.random.rand()

        if trial_prob <= probability:
            lattice.lattice_grid[i,j] *= -1

def evolve_and_plot(lattice, times, betaJ, betaMuH):
    """Evolves the diagram using the metropolis-hastings and plots the grid for the given input values of time"""
    
    #Set up the subplots: we need the number of times
    n = len(times)
    fig, ax = plt.subplots(1, n+1, figsize=(n*5, 5))
    
    computation_times = []

    t = 0
    tmax = max(times)
    index = 0
    
    start_time = time.time()

    while t < tmax:
        try_flip(lattice, betaJ, betaMuH)
        t = t+1

        if t in times:
            """Plots the grid every time the t counter coincides with one of the values inside the times array"""
            end_time = time.time()
            elapsed_time = end_time - start_time
            computation_times.append(elapsed_time)
            
            #Restart the clocks!
            start_time = time.time()

            grid = lattice.lattice_grid
            im = ax[index].matshow(grid, cmap="gray")
            ax[index].set_title(f"Time = {t}. \n Computational time = \n {elapsed_time:.3f}.")
            
            #Increments index to prevent each subsequent plot from overriding the others
            index += 1

    ax[n].plot(times,computation_times)
    ax[n].set_title("t value vs computation time")
    plt.show()



