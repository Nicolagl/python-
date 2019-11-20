
class wht:
    def __init__(self,age=1,sex="nan",hei=150):
        self.age=age
        self.sex=sex
        self.hei=hei
    def getage(self):
        return self.age
    def getsex(self):
        return self.sex
    def sethei(self,hei):
        self.hei=hei

c1=wht()

print(c1.age)
print(c1.sex)
c2=wht(22,"nv",175)
print(c2.age)
print(c2.sex)
