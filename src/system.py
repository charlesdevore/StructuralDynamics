""""system.py

Provide a system interface and class implementation for dynamic
systems.
"""

from abc import ABCMeta
from abc import abstractmethod
import pint
from constants import Mass
from constants import Damping
from constants import Stiffness

class SystemMetaClass(metaclass=ABCMeta):
    @abstractmethod
    def mass(self):
        raise NotImplemented

    @abstractmethod
    def damping(self):
        raise NotImplemented

    @abstractmethod
    def stiffness(self):
        raise NotImplemented

    @abstractmethod
    def initial_conditions(self):
        raise NotImplemented

class System(SystemMetaClass):
    _registry = None
    
    def registry(self):
        if not self._registry:
            self._registry = pint.UnitRegistry()
        return self._registry
    
    def _process_constant(self, quantity, class_type):
        if isinstance(quantity, class_type) and quantity._registry is self.registry():
            return quantity
        else:
            registry = self.registry()
            return class_type(registry, quantity)
                          

class SDOF(System):
    def __init__(self, m, c, k, initial_conditions=None, registry=None):

        if registry:
            self._registry = registry

        if initial_conditions:
            self._initial_conditions = initial_conditions
        else:
            self._initial_conditions = SDOFInitialConditions(None, None, self.registry())

        self._mass = self._process_constant(m, Mass)
        self._damping = self._process_constant(c, Damping)
        self._stiffness = self._process_constant(k, Stiffness)
        
        
    def initial_conditions(self):
        u0 = self._initial_conditions.initial_displacement
        v0 = self._initial_conditions.initial_velocity

        return u0, v0

    def mass(self):
        return self._mass

    def damping(self):
        return self._damping

    def stiffness(self):
        return self._stiffness
    

class InitialConditionsMetaClass(metaclass = ABCMeta):
    @abstractmethod
    def initial_displacement(self):
        raise NotImplemented

    @abstractmethod
    def initial_velocity(self):
        raise NotImplemented

    
class SDOFInitialConditions(InitialConditionsMetaClass):
    _registry=None

    def __init__(self, u0, v0, registry):

        self._registry = registry
        
        if u0:
            self._u0 = registry(u0)
        else:
            self._u0 = registry('0 m')

        if v0:
            self._v0 = registry(v0)
        else:
            self._v0 = registry('0 m/s')

    def initial_displacement(self):
        return self._u0

    def initial_velocity(self):
        return self._v0
