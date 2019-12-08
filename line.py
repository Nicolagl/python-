class Node():
    def __init__(self,data,next = None):
        self.data=data
        self.next=next

node1=Node(5)
node2=Node(4,node1)

print(node1.data,node2.data,"next is",node1.next,"node2 next",node2.next.data)

head=None
me=None
for i in range(1,5):
    head=Node(i,head)




new=Node(897)
print("new.data is",new.data)
while head!=None:
    if head.data==3:       
        new.next=head.next
        head.next=new
    if head.next==None:
        break
    print("head.data is",head.data)
    head=head.next

print("head.data is",head.data)

while head!=None:
    
    print(head.data)
    head=head.next
