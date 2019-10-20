from PSO import PSO
from constants import constants
import matplotlib.pyplot as plt
import os
elems = []

directory = 'graphs'
if not os.path.exists(directory):
   os.makedirs(directory)

particleSwarmOpt = PSO()
for i in range(0,3):
    inertia = constants.switchIn()
    for j in range(0,3):
        comparate = constants.switchCom()
        for h in range(0,2):
            func = constants.switchFunc()
            print(i,3,j,3,h,2)
            listelems = particleSwarmOpt.run()
            elems.append((listelems,inertia+comparate+func))
for elem in elems:
    plt.plot(elem[0])
    plt.savefig(os.path.join(directory,elem[1]+'.png'))
    plt.clf()
for elem in elems:
    plt.plot(elem[0])
plt.savefig(os.path.join(directory,'return.png'))
plt.clf()
