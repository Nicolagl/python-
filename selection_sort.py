def swap(lyst,i,j):
    temp=lyst[i]
    lyst[i]=lyst[j]
    lyst[j]=temp

def sels(lyst):
    i=0
    while i<len(lyst)-1:
        minindex=i
        j=i+1
        while j<len(lyst):
            if lyst[j]<lyst[minindex]:
                minindex=j
            j+=1
        if minindex !=i:
            swap(lyst,minindex,i)
        i+=1

list1=[1,5,4,8,9,6,54,5,4,2,45,3,0]

sels(list1)
print(list1)