list1=list([1,2,3])
print("list len is",len(list1),"max is",max(list1))
print(list1)
for i in range(0,3,1):
    list1[i]=list1[i]+i
print(list1)
list2=list1[1:3]#start to end-1
print(list2)
l4=list1+list2
l4.append(886)
l5=list2+list1
l6=list1.extend(list2)#can't def
print(l4,"uiuiuiu",l5,"l6 is",l6,list1)
list1.insert(0,554)
print(list1)
a=list1.pop(0)
print(a," ",list1)
l5.reverse( )
print(l5)
l5.sort()
print(l5)
