#linked list cycle II
#leetcode 142
def detectCycle(self, head):
    p1=head
    p2=head
    while p2 is not None and p2.next is not None:
        p1=p1.next
        p2=p2.next.next
        if p1==p2:
            p1=head
            while p1!=p2:
                p1=p1.next
                p2=p2.next
            return p1
    return None
          