def linearsearch(lst,key):
    for i in range(0,len(lst),1):
        if key == lst[i]:
            return i
    return -1
def insertsort(lst):
    for i in range(1,len(lst)):
        currentelement=lst[i]
        k=i-1
        while k>=0 and lst[k]>currentelement:
            lst[k+1]=lst[k]
            k-=1
        lst[k+1]=currentelement

list1=[]
for i in range(5):
    list1.append(int(input("请您丫输个数")))
print(linearsearch(list1,5))
insertsort(list1)
print(list1)
