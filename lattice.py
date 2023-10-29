import numpy as np
import matplotlib.pyplot as plt

class Lattice:
    """Lattice class"""

    def __init__(self, width, type):
        self.width = width
        self.type = type
        self.fig, self.ax = plt.subplots()

        """Type 1: a lattice where all of the spins are spin-up. 
        Type 0: Spins are randomly assigned values of +1 or -1.
        Type -1: we have a lattice where all of the spins are spin-down."""

        if type == 0:
            lattice = np.random.randint(0,2, size = (self.width, self.width), dtype = int) - np.ones((width,width))

        if type == 1:
            lattice = np.ones((self.width, self.width), dtype = int)

        if type == -1:
            lattice = -1*np.ones((self.width, self.width), dtype = int)

        self.lattice = lattice
    
    def get_width(self):
        return self.width
    
    def get_magnetisation(self):
        """Returns mean magnetisation of spins on lattice sites by summing all sites and dividing through by the total number of lattice
        sites"""

        sites_sum = np.sum(self.lattice)
        sites_number = np.size(self.lattice)

        magnetisation = sites_sum / sites_number

        return magnetisation
    

    def neighboring_sites_sum(self, i, j):
        """Sums the spins on all neighbouring sites as per the prescription of the ising model. Takes into account periodic boundary conditions
        by "wrapping around" the lattice for cases on the edge of the lattice. Doesn't involve diagonally adjacent lattice sites."""

        neighbor_sum = 0
        width = self.get_width()
        lattice = self.lattice

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


    
    def plot_lattice(self):
        self.ax.matshow(self.lattice)
        