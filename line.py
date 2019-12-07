class Node():
    def __init__(self,data,next = None):
        self.data=data
        self.next=next

node1=Node(5)
node2=Node(4,node1)

print(node1.data,node2.data,"next is",node1.next,"node2 next",node2.next.data)