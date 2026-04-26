#leetcode 206
#reverse a linked list

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp=head
        prev=None
        
        while temp is not None:
            front=temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev    


