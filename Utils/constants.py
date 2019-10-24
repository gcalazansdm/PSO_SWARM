import numpy as np
import math
import Enuns


def random(min_value, max_value, dimensions):
    rValue = np.random.random(size=dimensions)
    rValue = rValue * (max_value - min_value) + min_value
    return rValue

def compare(a, b):
    rValue = a > b
    return rValue

class Constants():
    def __init__(self):
        self.initValue = np.inf
        self.functionTypes = [Enuns.FunctionsType.Sphere,Enuns.FunctionsType.Rastrigin]
        self.comunicationTypes = [Enuns.ComunicationType.LOCAL,Enuns.ComunicationType.GLOBAL,Enuns.ComunicationType.FOCAL]
        self.inertiaTypes = [Enuns.InertiaType.CONSTANT,Enuns.InertiaType.LINEAR,Enuns.InertiaType.CLERC]

        self.dimensions = 30
        self.particles = 30
        
        self.numSimulations = 10

        self.inertia = 0.8

        self.c1 = 2.05
        self.c2 = 2.05

        self.maxInteractions = 10000

        self.inertiaRange = (0.4, 0.9)
        
        self.neighborhood = 1

constants = Constants()
