import matplotlib.pyplot as plt
import Utils
import PSO
import os

directory = 'graphs'
if not os.path.exists(directory):
   os.makedirs(directory)
directoryglobal = os.path.join(directory,'global')
if not os.path.exists(directoryglobal):
   os.makedirs(directoryglobal)
directoryindividual = os.path.join(directory,'individual')
if not os.path.exists(directoryindividual):
   os.makedirs(directoryindividual)

particleSwarmOpt = PSO.Swarm()
for inertia in Utils.constants.inertiaTypes:
    for function in Utils.constants.functionTypes:
        elems = []
        ielems = []
        for comunication in Utils.constants.comunicationTypes:
            listelems,listindividualelems = particleSwarmOpt.run(inertia,comunication,function)
            elems.append((listelems,comunication.name))
            ielems.append((listindividualelems,comunication.name))
   
        for i in elems:
            funcselems = i[0]
            print(funcselems)
            print(i[1])
            plt.plot(funcselems, label=i[1])
        plt.legend()
        plt.savefig(os.path.join(directory,function.name+'_'+inertia.name+'.png'))
        plt.clf()
