class Node():
    def __init__(self,data,next = None):
        self.data=data
        self.next=next

node1=Node(5)
node2=Node(4,node1)

print(node1.data,node2.data,"next is",node1.next,"node2 next",node2.next.data)

head=None
me=None
head=Node(0)
me=Node(78,head)

print("me's data",me.data)
for i in range(1,5):
    head=Node(i,head)

aa=head
while aa!=None:
    print(aa.data)
    aa=aa.next
#链表如果用自身遍历查看就会消除，可用哨兵节点来遍历