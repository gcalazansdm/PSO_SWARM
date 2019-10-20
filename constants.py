from Function_enum import functions
from inertia_enum import Inertia
from Comunication_enum import Comunication as comunicationType

class Constants():
    def __init__(self):
        self.dimensions = 30
        self.particles = 30
        self.__functionTypes = [functions.Sphere,functions.Rastrigin]
        self.function = functions.Sphere
        self.__functionPos = 0

        self.numSimulations  = 10

        self.__inertiaTypes = [Inertia.CONSTANT,Inertia.LINEAR,Inertia.CLERC]
        self.inertiaType = Inertia.CONSTANT
        self.__inertiaPos = 0

        self.inertia = 1.0

        self.c1 = 2.05
        self.c2 = 2.05

        self.__r1 = 0.25
        self.__r2 = 0.25

        self.maxSpeed = 3
        self.maxInteractions = 200#10000

        self.inertiaRange = (0,1)

        self.localWeight = (self.c1,self.__r1)
        self.globalWeight = (self.c2,self.__r2)

        self.__comunicationTypes = [comunicationType.GLOBAL,comunicationType.LOCAL,comunicationType.FOCAL]
        self.comunication = comunicationType.LOCAL
        self.__comunicationPos = 0

        self.neighborhood=1
    def switchIn(self):
        self.inertiaType = self.__inertiaTypes[self.__inertiaPos %len(self.__inertiaTypes)]
        self.__inertiaPos = self.__inertiaPos + 1
        return str(self.inertiaType)
    def switchFunc(self):
        self.function = self.__functionTypes[self.__functionPos %len(self.__functionTypes)]
        self.__functionPos = self.__functionPos + 1
        return str(self.function)
    def switchCom(self):
        self.comunication = self.__comunicationTypes[self.__comunicationPos %len(self.__comunicationTypes)]
        self.__comunicationPos = self.__comunicationPos + 1
        return str(self.comunication)
constants = Constants()
