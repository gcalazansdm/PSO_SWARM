import matplotlib.pyplot as plt
import Utils
import PSO
import os

directory = 'graphs/function'
if not os.path.exists(directory):
   os.makedirs(directory)
directoryboxplot = 'graphs/boxplot'
if not os.path.exists(directoryboxplot):
   os.makedirs(directoryboxplot)

particleSwarmOpt = PSO.Swarm()
for inertia in Utils.constants.inertiaTypes:
    for function in Utils.constants.functionTypes:
        listselems = []
        subtitlesElems = []
        finals = []
        for comunication in Utils.constants.comunicationTypes:
            listelems,finalgbestLists = particleSwarmOpt.run(inertia,comunication,function)
            listselems.append(listelems)
            subtitlesElems.append(comunication.name)
            finals.append(finalgbestLists)
        for i in range(len(listselems)):
            funcselems = listselems[i]
            plt.plot(funcselems, label=subtitlesElems[i])
        plt.legend()
        plt.savefig(os.path.join(directory,function.name+'_'+inertia.name+'.png'))
        plt.clf()
        fig1, ax1 = plt.subplots()
        ax1.boxplot(finals)
        ax1.set_xticklabels(subtitlesElems)
        plt.savefig(os.path.join(directoryboxplot,function.name+'_'+inertia.name+'.png'))
        plt.clf()
