class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def traverse(self):
        if self.head is None:
            print("List is empty")
        else:
            current = self.head
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")

sll = SLL()
sll.append(10)
sll.append(20)
sll.append(30)
sll.traverse()               

   