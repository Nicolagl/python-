class Node():
    def __init__(self,data,next = None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev

head=None
me=None
head0=Node(0)


for i in range(1,5):
    head=Node(i,head,head)
    print(head.data)
for i in range(1,5):
    head.prev=head
    print(head.data)