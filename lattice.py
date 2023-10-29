import numpy as np
import matplotlib.pyplot as plt

class Lattice:
    """Lattice class"""

    def __init__(self, width, type):
        self.width = width
        self.type = type

        """Type 1: a lattice where all of the spins are spin-up. 
        Type 0: Spins are randomly assigned values of +1 or -1.
        Type -1: we have a lattice where all of the spins are spin-down."""

        if type == 0:
            lattice = 2*np.random.randint(0,2, size = (self.width, self.width), dtype = int) - np.ones((self.width, self.width))

        if type == 1:
            lattice = np.ones((self.width, self.width), dtype = int)

        if type == -1:
            lattice = -1*np.ones((self.width, self.width), dtype = int)

        self.lattice_grid = lattice
    
    def get_width(self):
        return self.width
    
    def get_magnetisation(self):
        """Returns mean magnetisation of spins on lattice sites by summing all sites and dividing through by the total number of lattice
        sites"""

        sites_sum = np.sum(self.lattice_grid)
        sites_number = np.size(self.lattice_grid)

        magnetisation = sites_sum / sites_number

        return magnetisation
    

    def neighboring_sites_sum(self, i, j):
        """Sums the spins on all neighbouring sites as per the prescription of the ising model. Takes into account periodic boundary conditions
        by "wrapping around" the lattice for cases on the edge of the lattice. Doesn't involve diagonally adjacent lattice sites."""

        neighbor_sum = 0
        width = self.get_width()
        grid = self.lattice_grid

        if i == 0 and j == 0:
            """Top left corner"""
            neighbor_sum = grid[0,1] + grid[1,0] + grid[0, width-1] + grid[width-1, 0]

        if i == width -1 and j == 0:
            """Top right corner"""
            neighbor_sum = grid[i-1, j] + grid[i, j+1] + grid[i, width-1] + grid[0,0]

        if i == width -1 and j == width-1:
            """Bottom right corner"""
            neighbor_sum = grid[width-1, 0] + grid[i, j-1] + grid[0, j] + grid[i-1, j]

        if i == 0 and j == width-1:
            """Bottom left corner"""
            neighbor_sum = grid[0,0] + grid[i+1, j] + grid[width-1, j] + grid[i, j-1]

        if i == 0 and j != 0: 
            """Far left column"""
            neighbor_sum = grid[i, j-1] + grid[i, j+1] + grid[i+1, j] + grid[width-1, j]

        if i == width-1 and j != 0:
            """Far right column"""
            neighbor_sum = grid[i, j-1] + grid[i, j+1] + grid[i-1, j] + grid[0, j]

        if i != 0 and j == 0:
            """Top row"""
            neighbor_sum = grid[i+1, j] + grid[i-1,j] + grid[i, j+1] + grid[i, width-1]

        if i != 0 and j == width-1:
            """Bottom row"""
            neighbor_sum = grid[i+1, j] + grid[i-1, j] + grid[i, j-1] + grid[i, 0]

        else:
            neighbor_sum = grid[i+1, j] + grid[i-1, j] + grid[i, j+1] + grid[i, j-1]

        return neighbor_sum

        