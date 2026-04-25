class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class SLL:
    def __init__(self):
        self.head = None


    def append(self, val):
        new_node = Node(val)
        if self.head is None:        
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def traverse(self):
        if self.head is None:
            print("List is empty")
        else:
            current = self.head
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")


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

    def delete(self,pos):
        if self.head is None:
            print("List is empty")
        elif pos == 0:
            self.head = self.head.next
        else:
            current = self.head
            prev = None
            count = 0
            while current is not None and count < pos:
                prev = current
                current = current.next
                count += 1
            if current is None:
                print("Position out of bounds")
            else:
                prev.next = current.next
    def delete_by_value(self,val):
        temp=self.head
        if self.head is None:
            print("List is empty")
        elif temp.next is not None:
            if temp.val==val:
                self.head=temp.next
                return
            else:
                found=False
                prev=None
                while temp is not None:
                    if temp.val==val:
                        found=True
                        break
                    prev=temp
                    temp=temp.next
                if found:
                    prev.next=temp.next
                    return
                else:
                    print("Value not found in the list")

sll = SLL()
sll.append(10)
sll.append(20)
sll.append(30)
sll.traverse()    