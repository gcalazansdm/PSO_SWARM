import numpy as np
import math
from numpy.random import randint as random
from inertia_enum import Inertia
from constants import constants
from functions import function
from constants import compare


class Particle:
    def __init__(self):
        self.__speed = random(low=-1*constants.maxSpeed, high=constants.maxSpeed, size=constants.dimensions)
        self.__lowerBond = function.bondaries()[0]
        self.__hiBond = function.bondaries()[1]
        self.__position = random(low=self.__lowerBond, high=self.__hiBond, size=constants.dimensions)
        self.__fitness = constants.initValue
        self.__bestFitness = constants.initValue
        self.__boundaries = function.bondaries()
        self.__pBest = self.__position
        self.inertia = 0
        

    def updateInertia(self,interaction):
        if Inertia.CONSTANT == constants.inertiaType:
            self.inertia = constants.inertia
        elif Inertia.LINEAR == constants.inertiaType:
            self.inertia = constants.inertiaRange[1] - interaction *(constants.inertiaRange[1] - constants.inertiaRange[0]) / constants.maxInteractions
        elif Inertia.LINEAR == constants.inertiaType:
            phi = constants.c1 + constants.c2
            self.inertia = 2 / abs( 2 - phi - math.sqrt( phi* (phi-4) ) )
            
    def updateVelocity(self,gBest):
        self.__speed = self.inertia * self.__speed + constants.localWeight[0] * constants.localWeight[1]* ( np.subtract( self.__position, self.__pBest) )+ constants.globalWeight[0]*constants.globalWeight[1]*(np.subtract(self.__position,gBest))
        self.__speed = np.minimum(self.__speed,np.ones(self.__position.shape)*constants.maxSpeed)
        self.__speed = np.maximum(self.__speed,-1*np.ones(self.__position.shape)*constants.maxSpeed)

    def updatePossition(self):
        self.__position = np.sum((self.__position,self.__speed),axis=0)
        self.__position = np.minimum(self.__position,np.ones(self.__position.shape)*self.__hiBond)
        self.__position = np.maximum(self.__position,-1*np.ones(self.__position.shape)*self.__lowerBond)

    def updateFitness(self):
        self.__fitness = function.fitness(self.__position)
        
        if(compare(self.__bestFitness,self.__fitness)):
            self.__bestFitness = self.__fitness
            self.__pBest = self.__position
	
    def getBestFitness(self):
        return self.__bestFitness

    def getFitness(self):
        return self.__fitness

    def getbestPos(self):
        return self.__pBest
