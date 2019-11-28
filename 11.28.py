#继承与多态
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

def main():
    a=GeometricObject("sdsd",True)
    a.setcolor("whtsb")
    b=a.getcolor()
    print(a.color,b)
    rectangle=Rectangle(5,7)
    print("color:",rectangle.getcolor(),"area=",rectangle.getwidth())
 
main()
