def linearsearch(lst,key):
    for i in range(0,len(lst),1):
        if key == lst[i]:
            return i
    return -1
list1=[]
for i in range(5):
    list1.append(int(input()))
print(linearsearch(list1,5))
