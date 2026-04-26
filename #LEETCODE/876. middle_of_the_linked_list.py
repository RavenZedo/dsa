#middle of the linked list
#leetcode 876
def middleNode(self, head):
    n=0
    temp =self.head
    while temp is not None:
        temp = temp.next
        n+=1
    temp = self.head
    for i in range(n//2):
        temp=temp.next
    return temp
