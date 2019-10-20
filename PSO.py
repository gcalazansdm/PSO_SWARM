from Population import Population

from constants import constants

from time import clock
import numpy as np
import sys
import functools

def secondsToStr(t):
    return "%d:%02d:%02d.%03d" % \
        functools.reduce(lambda ll,b : divmod(ll[0],b) + ll[1:],
            [(t*1000,),1000,60,60])

def updateBar(progress,toolbar_width,loss,start=0):
    slices = int(float(progress)/toolbar_width * 50)
    write = "[%s%s]" % ("#"*slices," " * (50-slices))
    if(loss is not None):
        if(float(progress) > 0):
            write += " -> ("
            for elem in loss:
                write += "%f," % (float(elem)/progress)
            write += "\b)"
    else:
        write += " -> %d/%d" % (progress,toolbar_width)
    write += " %s" % secondsToStr(clock() - start)
    sys.stdout.write(write)
    sys.stdout.flush()
    sys.stdout.write("\b" * (len(write)+1)) # return to start of line, after '['


class PSO():
    
    def __init__(self):
        self.population = None

    def run(self):
       gBestLists = np.zeros(constants.maxInteractions)
       for i in range(constants.numSimulations):
           self.population = Population() #inicia particulas
           interaction = 0
           print(i,",",constants.numSimulations)
           updateBar(interaction,constants.maxInteractions,None)
           
           while interaction < constants.maxInteractions:
                self.population.updateInertia(interaction)#atualiza inercia

                self.population.updateFitness()#atualiza Fitness

                actualGbest = self.population.getbestFitness()
                actualpbest = self.population.getFitness()
                gBestLists[interaction] += (actualGbest)/constants.numSimulations#armazena melhor fitness
                
                self.population.updateVelocities()#atualiza velocidade
                self.population.updatePositions()#atualiza poiscoes
                updateBar(interaction,constants.maxInteractions,[actualGbest,actualpbest])
                interaction += 1
           print()
       return gBestLists
