import numpy as np

import Utils
import Enuns

class Function():
    def __init__(self,functionType):
        self.type = functionType
        
    def maxSpeed(self,SpeedLimitator=0.5):
        rValue = SpeedLimitator*(self.bondaries()[1]-self.bondaries()[0])
        return (-rValue,rValue)
		
    def bondaries(self):
        if self.type==Enuns.FunctionsType.Sphere:
            rValue = (-5.12, 5.12)
        else:
            rValue = (-5.12, 5.12)
        return rValue

    def fitness(self,x):
        if self.type==Enuns.FunctionsType.Sphere:
            rValue = np.sum(np.power(x,2),axis=None)
        else:
            a_1 = 10
            a = 10
            rValue = a*x.shape[0]+np.sum( np.subtract(np.power(x,2) , (a_1*np.cos(2*np.pi*x) )),axis=None)
        return rValue