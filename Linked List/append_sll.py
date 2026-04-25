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