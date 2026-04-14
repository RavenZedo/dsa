#majority element
#leetcode 169
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        candi=None
        
        for num in nums:
            if count==0:
               candi=num
            if num == candi:
                count+=1
            else:
                count-=1    
        return candi 

