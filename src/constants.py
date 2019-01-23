"""constants.py

Provide a collection of classes that provide unit tracking of constant
value numbers. These classes are implement using a template defined
by ConstantMetaClass and implemented using the Pint modulee in Python
repositories.
"""

import pint
from abc import ABCMeta
from abc import abstractmethod

class ConstantMetaClass(metaclass=ABCMeta):
    @abstractmethod
    def to(self, unit_str):
        raise NotImplemented

class Constant(ConstantMetaClass):
    def __init__(self, registry, input_str):
        # check input
        if not (self._check_registry(registry)
                and type(input_str) is str):
            print('Registry: {}'.format(registry))
            print('Input: {}'.format(input_str))
            raise InputError
        
        self._registry = registry
        self._quantity = self._registry(input_str)

    # def __eq__(self, other):
    #     return self._quantity == other._quantity

    # def __mul__(self, other):
    #     return self._quantity * other._quantity

    # def __pow__(self, other):
    #     return self._quantity ** other

    # def __add__(self, other):
    #     return self._quantity + other._quantity
        
    def _check_registry(self, registry):
        return isinstance(registry, pint.registry.UnitRegistry)
        
    def to(self, unit_str):
        return self._quantity.to(unit_str).magnitude

class Mass(Constant):
    def __init__(self, registry, input_str):
        C = Constant(registry, input_str)

        dimension = pint.unit.UnitsContainer({'[mass]':1.0})
        if not C._quantity.dimensionality == dimension:
            raise InputError

        self._quantity = C._quantity
        self._registry = C._registry

class Damping(Constant):
    def __init__(self, registry, input_str):
        C = Constant(registry, input_str)

        dimension = pint.unit.UnitsContainer({'[mass]':1.0,
                                              '[time]':-1.0})
        if not C._quantity.dimensionality == dimension:
            raise InputError

        self._quantity = C._quantity
        self._registry = C._registry

class Stiffness(Constant):
    def __init__(self, registry, input_str):
        C = Constant(registry, input_str)

        dimension = pint.unit.UnitsContainer({'[mass]':1.0,
                                              '[time]':-2.0})
        if not C._quantity.dimensionality == dimension:
            raise InputError

        self._quantity = C._quantity
        self._registry = C._registry

class Force(Constant):
    def __init__(self, registry, input_str):
        C = Constant(registry, input_str)

        dimension = pint.unit.UnitsContainer({'[mass]':1.0,
                                              '[length]':1.0,
                                              '[time]':-2.0})
        if not C._quantity.dimensionality == dimension:
            raise InputError

        self._quantity = C._quantity
        self._registry = C._registry



class Displacement(Constant):
    def __init__(self, registry, input_str):
        C = Constant(registry, input_str)

        dimension = pint.unit.UnitsContainer({'[length]':1.0})
        if not C._quantity.dimensionality == dimension:
            raise InputError

        self._quantity = C._quantity
        self._registry = C._registry


class Velocity(Constant):
    def __init__(self, registry, input_str):
        C = Constant(registry, input_str)

        dimension = pint.unit.UnitsContainer({'[length]':1.0,
                                              '[time]':-1.0})
        if not C._quantity.dimensionality == dimension:
            raise InputError

        self._quantity = C._quantity
        self._registry = C._registry


class Acceleration(Constant):
    def __init__(self, registry, input_str):
        C = Constant(registry, input_str)

        dimension = pint.unit.UnitsContainer({'[length]':1.0,
                                              '[time]':-2.0})
        if not C._quantity.dimensionality == dimension:
            raise InputError

        self._quantity = C._quantity
        self._registry = C._registry


