class Node():
    def __init__(self,data,next = None):
        self.data=data
        self.next=next

node1=Node(5)
node2=Node(4,node1)

print(node1.data,node2.data,"next is",node1.next,"node2 next",node2.next.data)

head=None
for i in range(1,5):
    head=Node(i,head)
while head!=None:
    print(head.data)
    head=head.next