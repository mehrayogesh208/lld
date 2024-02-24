from abc import ABC
class BasePizza(ABC):
    def cost(self):
        pass 

class FarmHouse(BasePizza):
    def cost(self):
        return 150
class Marghretia(BasePizza):
    def cost(self):
        return 250
class DecoratorPizza(BasePizza):
    def __init__(self):
        pass
    def cost(self):
        pass

class Cheese(DecoratorPizza):
    def __init__(self,pizza:BasePizza):
        self.basePizza = pizza
    def cost(self):
        return self.basePizza.cost()+100
    
class Veggies(DecoratorPizza):
    def __init__(self,pizza:BasePizza):
        self.basePizza = pizza
    def cost(self):
        return self.basePizza.cost()+200

if __name__ == '__main__':
    cost = Veggies(Cheese(Marghretia())).cost()
    print(cost)




