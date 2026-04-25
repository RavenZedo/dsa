class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class SLL:
    def __init__(self):
        self.head = None



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