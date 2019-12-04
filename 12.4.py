class GeometricObject:
    def __init__(self,color="green",filled=1):
        self.color=color
        self.filled=filled
    def getcolor(self):
        return self.color
    def setcolor(self,color):
        self.color=color
    def isfilled(self):
        return self.filled
    def setfilled(self,filled):
        self.filled=filled


class Rectangle(GeometricObject):
    def __init__(self,width=1,height=1):
        super( ).__init__()
        self.width=width
        self.height=height
    def getwidth(self):
        return self.width
    def setwidth(self,width):
        self.width=width
    def getheight(self):
        return self.height
    def setheight(self,height):
        self.height=height
    def getarea(self):
        return self.height*self.width
def un():
    s0=set()
    s1={1,5,5,55}
    s2={7,5,66}
    print(s1)
    s3=s1^s2
    s4=s1&s2
    print(s3,s4)
def main():
   #元组与集合 
    rectangles=(Rectangle(5,7),Rectangle(7,8),Rectangle(6,76))
    print("width=",rectangles[0].getwidth())
    rectangles[0].setwidth(1449)
    print("width=",rectangles[0].getwidth())
    un()
main()
