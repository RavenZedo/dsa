#leetcode 21
#merge two sorted linked list
def mergeTwoLists(self, l1, l2):
    dummy = ListNode(0)
    tail = dummy
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            tail=l1
            l1 = l1.next
        else:
            tail.next = l2
            tail=l2
            l2 = l2.next
    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2
    return dummy.next
