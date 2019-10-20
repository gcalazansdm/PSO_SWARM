import numpy as np
import math

from Particle import Particle

from constants import constants
from constants import compare
from numpy.random import randint as random
from Comunication_enum import Comunication as comunicationType

class Population():
    def __init__(self):
        self.particles = []
        for i in range(constants.dimensions):
            self.particles.append(Particle())
        self.comunication = constants.comunication
    
    def comparePositions(self,gBestFitness,BestPos,index,getBestFitness=True):
        rValue = (gBestFitness,BestPos)
        if(getBestFitness):
            gBest = self.particles[index].getBestFitness()
        else:
            gBest = self.particles[index].getFitness()                    
        if(compare(gBestFitness,gBest)): 
            rValue = (gBest,self.particles[index].getbestPos())
        return rValue

    def getbestFitness(self):
        gBest = constants.initValue     
        for i in range(constants.dimensions):
            gBest,_ = self.comparePositions(gBest,None,i)
        return gBest

    def getFitness(self):
        gBest = constants.initValue     
        for i in range(constants.dimensions):
            gBest,_ = self.comparePositions(gBest,None,i,getBestFitness=False)
        return gBest

    def updateVelocities(self):
        if self.comunication == comunicationType.GLOBAL:
            gBestFitness = constants.initValue   
            pBest = None    
            for i in range(constants.dimensions):
                gBestFitness,pBest = self.comparePositions(gBestFitness,pBest,i)
                
            for i in range(constants.dimensions):
               self.particles[i].updateVelocity(pBest)

        elif self.comunication == comunicationType.LOCAL:
            for i in range(constants.dimensions):
                gBestFitness = self.particles[i].getBestFitness()
                pBest = self.particles[i].getbestPos()  
                for j in range(constants.neighborhood):
                    left = max(i-j,0)
                    gBestFitness,pBest = self.comparePositions(gBestFitness,pBest,left)
                    
                    right = min(i+j,constants.dimensions-1)
                    gBestFitness,pBest = self.comparePositions(gBestFitness,pBest,right)

                self.particles[i].updateVelocity(pBest)
        else:
            focalPos = random(low=0, high=constants.dimensions-1, size=1)[0] 
            gBestFitness = self.particles[focalPos].getBestFitness() 
            pBest = self.particles[focalPos].getbestPos()      
            for i in range(constants.dimensions):
                _,fBest = self.comparePositions(gBestFitness,pBest,i)
                self.particles[i].updateVelocity(fBest)

    def updatePositions(self):
        for i in range(constants.dimensions):
           self.particles[i].updatePossition()

    def updateFitness(self):
        for i in range(constants.dimensions):
           self.particles[i].updateFitness()

    def updateInertia(self,interaction):
        for i in range(constants.dimensions):
           self.particles[i].updateInertia(interaction)


