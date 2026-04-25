class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def insert(self,val,pos):
        new_node=Node(val)
        if pos==0:
            new_node.next=self.head
            self.head=new_node
        else:
            current =self.head
            prev=None
            count=0
            while current is not None and count<pos:
                prev=current
                current=current.next
                count+=1
            prev.next=new_node
            new_node.next=current    