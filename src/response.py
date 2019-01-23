"""
response.py

"""

import numpy as np
from abc import ABCMeta
from abc import abstractmethod
from constants import Displacement
from constants import Velocity
from constants import Acceleration

class ResponseMetaClass(metaclass=ABCMeta):
    def displacement(self):
        raise NotImplemented

    def velocity(self):
        raise NotImplemented

    def acceleration(self):
        raise NotImplemented

    def plot(self):
        raise NotImplemented

class Response(ResponseMetaClass):
    pass
    
class ResponseSDOF(Response):
    def __init__(self, load, system):

        
        t0 = 0.
        tf = 10.
        dt = 0.001

    
