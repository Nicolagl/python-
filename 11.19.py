import math
class circle:
    def __init__(self,radius=1):
        self.radius=radius
    def getperimeter(self):
        return 2*self.radius*math.pi
    def getarea(self):
        return self.radius*self.radius*math.pi
    def setradius(self,radius):
        self.radius=radius

c1=circle(5)
print(c1.getarea())
print(c1.radius)
