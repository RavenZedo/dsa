#remove element from array
#leetcode 27
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n=len(nums)
        i=0
        for j in range(0,n):
            if nums[j]!=val:
                nums[i]=nums[j]
                i+=1
        return i               


