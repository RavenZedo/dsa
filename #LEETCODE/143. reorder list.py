#reorder list
#leetcode 143
def reorderList(self, head):
    if not head:
        return None
    slow = head
    fast = head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    prev = None
    curr=slow.next
    slow.next=None
    while curr:
        front=curr.next
        curr.next=prev
        prev=curr
        curr=front 
    left=head
    right=prev
    while right:
        left_next=left.next
        right_next=right.next
        left.next=right
        right.next=left_next
        left=left_next
        right=right_next
    return head       