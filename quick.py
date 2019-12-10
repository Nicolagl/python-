def quick(lyst):
    quickhelper(lyst,0,len(lyst)-1)
def quickhelper(lyst,left,right):
    if left<right:
        pivotlocation=partition(lyst,left,right)
        quickhelper(lyst,left,pivotlocation-1)
        quickhelper(lyst,pivotlocation+1,right)
def partition(lyst,left,right):
    #find the pivot and exchange it with the ast item
    middle=(left+right)//2
    pivot=lyst[middle]
    lyst[middle]=lyst[right]
    lyst[right]=pivot
    #set boundary=left
    boundary=left
    #move items less than pivot to the left
    for index in range(left,right):
        if lyst[index]<pivot:
            swap(lyst,index,boundary)
            boundary+=1
    #exchange the pivot item and the boundary item
    swap(lyst,right,boundary)
    return boundary
#earlier definition of the swap function goes here

def swap(lyst,i,j):
    temp=lyst[i]
    lyst[i]=lyst[j]
    lyst[j]=temp

list1=[1,5,4,8,9,6,54,5,4,2,45,3,0]


quick(list1)
print(list1)