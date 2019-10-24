import numpy as np
import math
import Enuns
import Utils

class Particle:
    def __init__(self,inertia,functionType):
        self.__function = Utils.Function(functionType)
        self.__maxSpeed = self.__function.maxSpeed()
        self.__lowerBond = self.__function.bondaries()[0]
        self.__hiBond = self.__function.bondaries()[1]
        self.__speed = Utils.random(self.__maxSpeed[0], self.__maxSpeed[1],Utils.constants.dimensions)
        self.__position = Utils.random(self.__lowerBond, self.__hiBond, Utils.constants.dimensions)
        self.__fitness = Utils.constants.initValue
        self.__bestFitness = Utils.constants.initValue
        self.__pBest = self.__position
        self.__inertiaType  = inertia
        self.inertia = 0

    def defPos(self,pos):
        self.__position = pos

    def updateInertia(self, interaction):
        if Enuns.InertiaType.CONSTANT == self.__inertiaType:
            self.inertia = Utils.constants.inertia
        elif Enuns.InertiaType.LINEAR == self.__inertiaType:
            self.inertia = Utils.constants.inertiaRange[1] - interaction * (
                        Utils.constants.inertiaRange[1] - Utils.constants.inertiaRange[0]) / Utils.constants.maxInteractions
        elif Enuns.InertiaType.CLERC == self.__inertiaType:
            phi = Utils.constants.c1 + Utils.constants.c2
            self.inertia = 2 / abs(2 - phi - math.sqrt(phi * (phi - 4)))

    def updateVelocity(self, gBest):
        r1 = Utils.random(0,1,Utils.constants.dimensions)
        r2 = Utils.random(0,1,Utils.constants.dimensions)

        selfValue = self.inertia * self.__speed
        localValue = Utils.constants.c1 * r1 * np.subtract(self.__pBest, self.__position)
        globalValue = Utils.constants.c2 * r2 * np.subtract(gBest, self.__position)

        self.__speed = selfValue + localValue + globalValue
        self.__speed = np.maximum(self.__speed, np.ones(self.__position.shape) * self.__maxSpeed[0])
        self.__speed = np.minimum(self.__speed, np.ones(self.__position.shape) * self.__maxSpeed[1])

    def updatePossition(self):
        self.__position = np.sum((self.__position, self.__speed), axis=0)
        self.__position = np.minimum(self.__position, np.ones(self.__position.shape) * self.__hiBond)
        self.__position = np.maximum(self.__position, np.ones(self.__position.shape) * self.__lowerBond)

    def updateFitness(self):
        self.__fitness = self.__function.fitness(self.__position)
        if (Utils.compare(self.__bestFitness, self.__fitness)):
            self.__bestFitness = self.__fitness
            self.__pBest = self.__position

    def getBestFitness(self):
        return self.__bestFitness

    def getFitness(self):
        return self.__fitness

    def getbestPos(self):
        return self.__pBest
