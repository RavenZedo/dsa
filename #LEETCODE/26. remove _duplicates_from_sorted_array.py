#remove duplicates from sorted array
#leetcode 26
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        nums.sort()
        i=0
        j=i+1
        while j<n:
            if nums[i]!=nums[j]:
                i+=1
                nums[i]=nums[j]
            j+=1
        return i+1 