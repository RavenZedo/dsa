#lc=92
#reverse linked list II
def reverseBetween(self,head,left,right):
    dummy = ListNode(0,head)
    left_prev=dummy
    current=head
    for _ in range(left-1):
        left_prev=current
        current=current.next
    prev=None
    for _ in range(right-left+1):
        temp_next=current.next
        current.next=prev
        prev=current
        current=temp_next 
    left_prev.next.next=current
    left_prev.next=prev