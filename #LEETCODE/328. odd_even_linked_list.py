#leetcode 328
#odd even linked list
def oddEvenList(self, head):
    if not head:
        return None
    odd = head
    even=head.next
    even_head=even
    while even is not None and even.next is not None:
        odd.next=odd.next.next
        odd=odd.next
        even.next=even.next.next
        even=even.next
    odd.next=even_head
    return head