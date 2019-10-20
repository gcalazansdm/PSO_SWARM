import numpy as np

from Function_enum import functions
from constants import constants

class Function():
    def bondaries(self):
        return (-5.12, 5.12)

    def fitness(self,x):
        rValue = -np.inf
        if constants.function==functions.Sphere:
            rValue = np.sum(np.power(x,2),axis=None) 
        else:
            a_1 = 10
            rValue = a_1+np.sum( np.subtract(np.power(x,2) , (10*np.cos(2*np.pi*x) )),axis=None)
            
        return rValue

function = Function() 
