# SDOF_response.py

"""
Set of functions used for generating the response of a SDOF
system. This set of modules will be superseded by a class architecture
in later versions. Included to demonstrate behavior and facilitate
testing.  
"""

import numpy as np

def compute_response(system, load, t0, dt, tf):

    


class System(object):
    def __init__(m, c, k):
        self.mass = m
        self.damping = c
        self.stiffness = k

    @property
    def natural_frequency(self):

        Wn = np.sqrt(self.stiffness / self.mass)
        
        return Wn

    @property
    def damping_ratio(self):

        Wn = self.natural_frequency()

        zeta = self.damping / (2 * self.mass * Wn)

        return zeta

    @property
    def damped_natural_frequency(self):

        Wn = self.natural_frequency()
        zeta = self.damping_ratio()

        Wd = Wn * np.sqrt(1-zeta**2)

        return Wd


class Load(object):
    def __init__(p0):
        self.load_max = p0


    def load_value(self, time):
        if time > 0:
            return self.load_max
        else:
            return 0

        
    
        
