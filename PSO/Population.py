import numpy as np
import math

from PSO.Particle import Particle
import Utils
import Enuns

class Population():
    def __init__(self,inertia,comunication,function):
        self.particles = []
        for i in range(Utils.constants.particles):
            self.particles.append(Particle(inertia,function))
        self.comunication = comunication
    
    def comparePositions(self,gBestFitness,BestPos,index,getBestFitness_=True):
        rValue = (gBestFitness,BestPos)
        if(getBestFitness_):
            gBest = self.particles[index].getBestFitness()
        else:
            gBest = self.particles[index].getFitness()   
        if(Utils.compare(gBestFitness,gBest)): 
            rValue = (gBest,self.particles[index].getbestPos())
        return rValue

    def getbestFitness(self):
        gBest = Utils.constants.initValue     
        for i in range(Utils.constants.particles):
            gBest,_ = self.comparePositions(gBest,None,i)
        return gBest

    def getFitness(self):
        fitness = Utils.constants.initValue     
        for i in range(Utils.constants.particles):
            fitness,_ = self.comparePositions(fitness,None,i,False)
        return fitness

    def updateVelocities(self):
        if self.comunication == Enuns.ComunicationType.GLOBAL:
            gBestFitness = Utils.constants.initValue   
            gBest = None    
            for i in range(Utils.constants.particles):
                gBestFitness,gBest = self.comparePositions(gBestFitness,gBest,i)
                
            for i in range(Utils.constants.particles):
               self.particles[i].updateVelocity(gBest)

        elif self.comunication == Enuns.ComunicationType.LOCAL:
            for i in range(Utils.constants.particles):
                gBestFitness = self.particles[i].getBestFitness()
                gBest = self.particles[i].getbestPos()  
                for j in range(Utils.constants.neighborhood):
                    left = i-j-1
                    if(left < 0):
                        left = Utils.constants.particles + left
                    gBestFitness,gBest = self.comparePositions(gBestFitness,gBest,left)
                    
                    right = i+j-1
                    if(right > Utils.constants.particles):
                        right = right - Utils.constants.particles
                    gBestFitness,gBest = self.comparePositions(gBestFitness,gBest,right)

                self.particles[i].updateVelocity(gBest)
        else:
            focalPos = int(round(Utils.random(0, Utils.constants.particles-1, 1)[0]))
            gBestFitness = self.particles[focalPos].getBestFitness() 
            gBest = self.particles[focalPos].getbestPos()      
            for i in range(Utils.constants.particles):
                _,fBest = self.comparePositions(gBestFitness,gBest,i)
                self.particles[i].updateVelocity(fBest)

    def updatePositions(self):
        for i in range(Utils.constants.particles):
           self.particles[i].updatePossition()

    def updateFitness(self):
        for i in range(Utils.constants.particles):
           self.particles[i].updateFitness()

    def updateInertia(self,interaction):
        for i in range(Utils.constants.particles):
           self.particles[i].updateInertia(interaction)


