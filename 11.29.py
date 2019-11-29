class A:
    def __init__(self,i=0):
        self.i=i
    def ml(self):
        self.i+=1
class B(A):
    def __init__(self,j=0):
        super().__init__(3)
        self.j=j
    #def ml(self):
        #self.i+=1
def main():
    b=B()
    b.ml()
    print(b.j)
    print(b.i)
main()
