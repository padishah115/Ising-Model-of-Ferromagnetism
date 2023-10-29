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
    
    def plot_lattice(self):
        self.ax.matshow(self.lattice)
        