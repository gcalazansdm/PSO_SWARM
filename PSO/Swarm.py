from PSO.Population import Population
import Utils

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
                write += "%f," % (float(elem))
            write += "\b)"
    else:
        write += " -> %d/%d" % (progress,toolbar_width)
    write += " %s" % secondsToStr(clock() - start)
    sys.stdout.write(write)
    sys.stdout.flush()
    sys.stdout.write("\b" * (len(write)+1)) # return to start of line, after '['


class Swarm():
    def run(self,inertia,comunication,function):
       gBestLists = np.zeros(Utils.constants.maxInteractions)
       finalgbestLists = np.zeros(Utils.constants.numSimulations)
       for i in range(Utils.constants.numSimulations):
           population = Population(inertia,comunication,function) #inicia particulas
           interaction = 0
           print(i,",",Utils.constants.numSimulations)
           updateBar(interaction,Utils.constants.maxInteractions,None)
           
           while interaction < Utils.constants.maxInteractions:
                
#                print("\ninteraction",interaction)
                population.updateInertia(interaction)#atualiza inercia

                population.updateFitness()#atualiza Fitness

                actualGbest = population.getbestFitness()
                actualpbest = population.getFitness()
                gBestLists[interaction] = gBestLists[interaction] +(actualGbest)/Utils.constants.numSimulations#armazena melhor fitness
                population.updateVelocities()#atualiza velocidade
                population.updatePositions()#atualiza poiscoes
                updateBar(interaction,Utils.constants.maxInteractions,[actualGbest,actualpbest])
                interaction += 1
           print()
           finalgbestLists[i] = gBestLists[interaction-1]
       return gBestLists,finalgbestLists
