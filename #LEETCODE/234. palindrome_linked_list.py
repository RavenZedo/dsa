#palindrome linked list
#leetcode 234
def isPalindrome(self, head):
    slow = head
    fast =head
    while fast is not None and fast.next is not None:
        slow=slow.next
        fast=fast.next.next
    prev=None
    while slow is not None:
        front=slow.next
        slow.next=prev
        prev=slow
        slow=front
    left=head   
    right=prev
    while right is not None:    
        if left.val!=right.val:
            return False
        left=left.next
        right=right.next    
    return True