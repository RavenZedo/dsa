class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

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





    