class car:
    def __init__(self,name,model,colour,cost):
        self.name=name
        self.model=model
        self.colour=colour
        self.cost=cost
    def display(self):
        print("car name is:",self.name)
        print("car model is:",self.model)
        print("car colour is:",self.colour)
        print("car cost is:",self.cost)
c1=car("Tesla","modelY","Black",1000000.0)
c1.display()
