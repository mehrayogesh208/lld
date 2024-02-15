from abc import ABC

#Statergy Interface
class navigateStatergy(ABC):
    def execute(self,A,B):
        pass

#Each algorithm is devided into different class
class Road(navigateStatergy):
    def execute(self,A,B):
        print("On Road ",A,B)

class OnFoot(navigateStatergy):
    def execute(self, A, B):
        print("On Foot ",A,B)

#Context Class in which statergy is passed via client while initialising the object
class context:
    def __init__(self,statergy:navigateStatergy):
        self._statergy = statergy
    def navigate(self,A,B):
        self._statergy.execute(A,B)

if __name__ == '__main__':
    contextObjRoad = context(Road())
    contextObjRoad.navigate("A","B")
    contextObjFoot = context(OnFoot())
    contextObjFoot.navigate("C","D")
    
